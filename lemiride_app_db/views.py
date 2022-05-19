import os
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.forms.models import model_to_dict
import razorpay
from uritemplate import partial

from .models import CustomerInformation, Localities, ProductDetails, TransactionDetails
from .serializers import CustomerInformationSerializer, LocalitiesSerializer, ProductDetailsSerializer, TransactionDetailsSerializer
from datetime import datetime


api_key = os.environ.get('RZP_ID')
api_secret = os.environ.get('RZP_PWD')
client = razorpay.Client(auth=(api_key, api_secret))



def index(request):
    return HttpResponse("Hello, world. You're at the LemiRideDB index.")

class CustomerInformationViews(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, number):
        customer, _ = CustomerInformation.objects.get_or_create(
        username=request.user,
        contact_number=number,
        defaults={'customer_name': '', 'email_id':''},
        )
        print(customer)

        serializer = CustomerInformationSerializer(customer)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request):
        customer_id = request.data['id']
        customer = CustomerInformation.objects.get(pk=customer_id)
        serializer = CustomerInformationSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, id=None):
    #     if id:
    #         customer = CustomerInformation.objects.get(username=request.user)
    #         serializer = CustomerInformationSerializer(customer)
    #         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    #     items = CustomerInformation.objects.all()
    #     serializer = CustomerInformationSerializer(items, many=True)
    #     return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class LocalitiesViews(APIView):
    
    def get(self, request):

        items = Localities.objects.all()
        serializer = LocalitiesSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class ProductDetailsViews(APIView):
    
    def get(self, request, location=None, city=None, day=None, month=None, year=None, hour=None, minute=None):

        if location:
            to_convert = f'{day}/{month}/{year} {hour}:{minute}'
            converted_time = datetime.strptime(to_convert, '%d/%m/%Y %H:%M')
            filtered_date = ProductDetails.objects.filter(available_from__lte = converted_time)
            
            if location == 'All':
                filtered_loc = filtered_date.filter(partner_info__locality__city__city=city)
            else:
                filtered_loc = filtered_date.filter(partner_info__locality__locality=location)
            
            serializer = ProductDetailsSerializer(filtered_loc, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = ProductDetails.objects.all()
        serializer = ProductDetailsSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request):
        product_id = request.data['id']
        product = ProductDetails.objects.get(pk=product_id)
        serializer = ProductDetailsSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




class UserViews(APIView):
    """ Simple endpoint to test auth """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """ Return request.user and request.auth """
        return Response({
            'request.user': model_to_dict(request.user),
            'request.auth': request.auth
        })

class TransactionCreate(APIView):
    '''Creates a transaction and returns transaction with order ID from razorpay - required to complete payment'''
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = TransactionDetailsSerializer(data=request.data)
        if serializer.is_valid():
            amt =float(serializer.validated_data['total_amount']) *100
            order_id = create_razorpay_order(amt)
            serializer.save(payment_reference=order_id)

            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        transaction_id = request.data['id']
        transaction = TransactionDetails.objects.get(pk=transaction_id)
        serializer = TransactionDetailsSerializer(transaction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




def create_razorpay_order(amount):
    DATA = {'amount': amount,'currency': 'INR' }
    rzp_response = client.order.create(DATA)
    order_id = rzp_response['id']

    return order_id