from datetime import datetime
from django.db import models


class PartnerInfo(models.Model):
    business_name = models.CharField('Business / Entity Name', max_length=100, unique=True)
    owner_name = models.CharField('Owner Name',max_length=100)
    mail_id = models.EmailField('Email ID', max_length=100)
    city = models.CharField('City', max_length=100)
    pincode = models.IntegerField('Pincode')
    whatsapp_number = models.IntegerField('Whatsapp Number')
    account_number = models.IntegerField('Account Number')
    ifsc_code = models.CharField('IFSC Code', max_length=100)
    upi_id = models.CharField('UPI ID', max_length=100)


    def __str__(self):
        return self.business_name

    class Meta:
        verbose_name_plural = "Partner Information"

class ProductCategory(models.Model):
    manufacturer = models.CharField('Manufacturer', max_length=100)
    model = models.CharField('Model', max_length=100)

    def __str__(self):
        return '{} - {}'.format(self.manufacturer, self.model)

    class Meta:
        verbose_name_plural = "Product Categories"

class ProductDetails(models.Model):
    product_category = models.ForeignKey(ProductCategory, on_delete=models.RESTRICT)
    rc_number = models.CharField('Vehicle / RC Number', max_length=100)
    pricing = models.FloatField('Pricing Weekday')

    def __str__(self):
        return self.rc_number

    class Meta:
        verbose_name_plural = "Product Details"

class CustomerInformation(models.Model):
    customer_name = models.CharField('Customer Name', max_length=100)
    contact_number = models.IntegerField('Mobile Number',  default=0)
    email_id = models.EmailField('Email ID', blank=True)
    driving_license_number = models.CharField('Driving License Number', max_length=100)
    

    def __str__(self):
        return '{} - {}'.format(self.customer_name, self.contact_number)

    class Meta:
        verbose_name_plural = "Customer Information"

class TransactionDetails(models.Model):
    BOOKING_STATUS = [('completed', 'Payment Completed'), ('picked', 'Picked Up'),  ('returned', 'Returned')]
    payment_type = models.CharField('Payment Type', max_length=100)
    payment_date = models.DateField('Payment Date', default=datetime.now, blank=True)
    payment_reference = models.CharField('Payment Reference', max_length=100)
    booking_date = models.DateField('Booking Date')
    pickup_date = models.DateField('Pick Up Date', blank=True, null=True)
    return_date = models.DateField('Return Date', blank=True, null=True)
    booking_status = models.CharField('Booking Status', choices=BOOKING_STATUS, default='Payment Complete', max_length=100)
    total_amount = models.FloatField('Total Amount')
    customer_information = models.ForeignKey(CustomerInformation, on_delete=models.RESTRICT)
    product_details = models.ForeignKey(ProductDetails, on_delete=models.RESTRICT)
    partner_info = models.ForeignKey(PartnerInfo, on_delete=models.RESTRICT)

    def __str__(self):
        return self.payment_reference
    
    class Meta:
        verbose_name_plural = "Transaction Details"
    

