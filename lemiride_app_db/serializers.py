from rest_framework import serializers
from .models import CustomerInformation, Localities, PartnerInfo, ProductDetails

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
        fields = ['locality', 'city']
    
class PartnerInfoSerializer(serializers.ModelSerializer):
    business_name = serializers.CharField(max_length=100)
    locality = LocalitiesSerializer(read_only=True)

    class Meta:
        model = PartnerInfo
        fields = ['business_name', 'locality']




class ProductDetailsSerializer(serializers.ModelSerializer):
    product_category = serializers.CharField(max_length=100)
    rc_number = serializers.CharField(max_length=100)
    pricing = serializers.FloatField()
    partner_info = PartnerInfoSerializer(read_only=True)
    available_from = serializers.DateTimeField()

    class Meta:
        model = ProductDetails
        fields = ('__all__')
    