from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomerInformation, Localities, ProductDetails
from .serializers import CustomerInformationSerializer, LocalitiesSerializer, ProductDetailsSerializer
from datetime import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the LemiRideDB index.")

class CustomerInformationViews(APIView):
    def post(self, request):
        serializer = CustomerInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            customer = CustomerInformation.objects.get(id=id)
            serializer = CustomerInformationSerializer(customer)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = CustomerInformation.objects.all()
        serializer = CustomerInformationSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class LocalitiesViews(APIView):

    def get(self, request):

        items = Localities.objects.all()
        serializer = LocalitiesSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class ProductDetailsViews(APIView):

    def get(self, request, location=None, day=None, month=None, year=None, hour=None, minute=None):

        if location:
            to_convert = f'{day}/{month}/{year} {hour}:{minute}'
            converted_time = datetime.strptime(to_convert, '%d/%m/%y %H:%M')
            filtered_date = ProductDetails.objects.filter(available_from__lte = converted_time)
            filtered_loc = filtered_date.filter(partner_info__locality__locality=location)
            
            serializer = ProductDetailsSerializer(filtered_loc, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = ProductDetails.objects.all()
        serializer = ProductDetailsSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
