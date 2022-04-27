from rest_framework import serializers
from .models import CustomerInformation

class CustomerInformationSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(max_length=100)
    contact_number = serializers.CharField(max_length=100)
    email_id = serializers.EmailField()
    driving_license_number = serializers.CharField(max_length=100)

    class Meta:
        model = CustomerInformation
        fields = ('__all__')
    