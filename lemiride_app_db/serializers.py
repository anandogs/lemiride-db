from pyexpat import model
from rest_framework import serializers
from .models import CustomerInformation, Localities, PartnerInfo, ProductDetails, ProductCategory, TransactionDetails

class CustomerInformationSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(max_length=100)
    contact_number = serializers.CharField(max_length=100)
    email_id = serializers.EmailField()
    class Meta:
        model = CustomerInformation
        fields = ['id', 'customer_name', 'contact_number', 'email_id']

class LocalitiesSerializer(serializers.ModelSerializer):
    locality = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    
    class Meta:
        model = Localities
        fields = ['id', 'locality', 'city']
    
class PartnerInfoSerializer(serializers.ModelSerializer):
    business_name = serializers.CharField(max_length=100)
    locality = LocalitiesSerializer(read_only=True)

    class Meta:
        model = PartnerInfo
        fields = ['business_name', 'locality']


class ProductCategorySerializer(serializers.ModelSerializer):
    manufacturer = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)
    image = serializers.CharField(max_length=100)

    
    class Meta:
        model = ProductCategory
        fields = ['manufacturer', 'model', 'image']




class ProductDetailsSerializer(serializers.ModelSerializer):
    product_category = ProductCategorySerializer(read_only=True)
    rc_number = serializers.CharField(max_length=100)
    pricing_weekday = serializers.FloatField()
    pricing_weekend = serializers.FloatField()
    deposit = serializers.FloatField()
    partner_info = PartnerInfoSerializer(read_only=True)
    available_from = serializers.DateTimeField()

    class Meta:
        model = ProductDetails
        fields = ('__all__')
    
class TransactionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=TransactionDetails
        fields=('id', 'payment_type','payment_date','payment_reference','booking_date','pickup_date','return_date','booking_status', 'total_amount', 'customer_information', 'product_details')

    def to_representation(self, instance):
        self.fields['customer_details'] =  CustomerInformationSerializer(read_only=True)
        return super().to_representation(instance)

    def to_representation(self, instance):
        self.fields['product_details'] =  ProductDetailsSerializer(read_only=True)
        return super().to_representation(instance)