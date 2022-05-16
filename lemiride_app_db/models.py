from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Cities(models.Model):
    city = models.CharField('City', max_length=100)

    def __str__(self) -> str:
        return self.city

    class Meta:
        verbose_name_plural = 'Cities'



class Localities(models.Model):
    locality = models.CharField('Locality', max_length=100)
    city = models.ForeignKey(Cities, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.locality

    class Meta:
        verbose_name_plural = 'Localities'


class PartnerInfo(models.Model):
    business_name = models.CharField('Business / Entity Name', max_length=100, unique=True)
    owner_name = models.CharField('Owner Name',max_length=100)
    mail_id = models.EmailField('Email ID', max_length=100)
    locality = models.ForeignKey(Localities, on_delete=models.RESTRICT)
    whatsapp_number = models.CharField('Whatsapp Number', max_length=100)
    account_number = models.CharField('Account Number', max_length=100)
    ifsc_code = models.CharField('IFSC Code', max_length=100)
    upi_id = models.CharField('UPI ID', max_length=100)


    def __str__(self):
        return self.business_name

    class Meta:
        verbose_name_plural = "Partner Information"

class ProductCategory(models.Model):
    manufacturer = models.CharField('Manufacturer', max_length=100)
    model = models.CharField('Model', max_length=100)
    image = models.FileField(upload_to='media/', default='')

    def __str__(self):
        return '{} - {}'.format(self.manufacturer, self.model)

    class Meta:
        verbose_name_plural = "Product Categories"

class ProductDetails(models.Model):
    product_category = models.ForeignKey(ProductCategory, on_delete=models.RESTRICT)
    rc_number = models.CharField('Vehicle / RC Number', max_length=100)
    pricing_weekday = models.FloatField('Pricing Weekday', default=0)
    pricing_weekend = models.FloatField('Pricing Weekend', default=0)
    deposit = models.FloatField('Deposit', default=0)
    partner_info = models.ForeignKey(PartnerInfo, on_delete=models.RESTRICT)
    available_from = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.rc_number

    class Meta:
        verbose_name_plural = "Product Details"

class CustomerInformation(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    customer_name = models.CharField('Customer Name', max_length=100)
    contact_number = models.CharField('Mobile Number', max_length=100)
    email_id = models.EmailField('Email ID', blank=True)
    

    def __str__(self):
        return '{} - {}'.format(self.customer_name, self.contact_number)

    class Meta:
        verbose_name_plural = "Customer Information"

class TransactionDetails(models.Model):
    BOOKING_STATUS = [('started', 'Payment Started'), ('completed', 'Payment Completed'), ('picked', 'Picked Up'),  ('returned', 'Returned')]
    payment_type = models.CharField('Payment Type', max_length=100, blank=True)
    payment_date = models.DateField('Payment Date', default=datetime.now, blank=True)
    payment_reference = models.CharField('Payment Reference', max_length=100, blank=True)
    booking_date = models.DateField('Booking Date', blank=True, null=True)
    pickup_date = models.DateField('Pick Up Date', blank=True, null=True)
    return_date = models.DateField('Return Date', blank=True, null=True)
    booking_status = models.CharField('Booking Status', choices=BOOKING_STATUS, default='Payment Started', max_length=100)
    total_amount = models.FloatField('Total Amount')
    customer_information = models.ForeignKey(CustomerInformation, on_delete=models.RESTRICT)
    product_details = models.ForeignKey(ProductDetails, on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.booking_status
    
    class Meta:
        verbose_name_plural = "Transaction Details"
    
