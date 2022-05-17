from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.forms.models import model_to_dict

from .models import CustomerInformation, Localities, ProductDetails
from .serializers import CustomerInformationSerializer, LocalitiesSerializer, ProductDetailsSerializer, TransactionDetailsSerializer
from datetime import datetime

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

    # def post(self, request):
    #     serializer = CustomerInformationSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    #     else:
    #         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

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
    
    def get(self, request, location=None, day=None, month=None, year=None, hour=None, minute=None):

        if location:
            to_convert = f'{day}/{month}/{year} {hour}:{minute}'
            converted_time = datetime.strptime(to_convert, '%d/%m/%Y %H:%M')
            filtered_date = ProductDetails.objects.filter(available_from__lte = converted_time)
            filtered_loc = filtered_date.filter(partner_info__locality__locality=location)
            
            serializer = ProductDetailsSerializer(filtered_loc, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = ProductDetails.objects.all()
        serializer = ProductDetailsSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


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
    def post(self, request):
        serializer = TransactionDetailsSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)