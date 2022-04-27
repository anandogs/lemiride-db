from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomerInformation
from .serializers import CustomerInformationSerializer

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

