from rest_framework import serializers
from .models import CustomerInformation, Localities

class CustomerInformationSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(max_length=100)
    contact_number = serializers.CharField(max_length=100)
    email_id = serializers.EmailField()
    driving_license_number = serializers.CharField(max_length=100)

    class Meta:
        model = CustomerInformation
        fields = ('__all__')

class LocalitiesSerializer(serializers.ModelSerializer):
    locality = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    
    class Meta:
        model = Localities
        fields = ('__all__')
    