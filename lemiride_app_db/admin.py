from django.contrib import admin

from .models import PartnerInfo, ProductCategory, ProductDetails, CustomerInformation, TransactionDetails, Localities, Cities

admin.site.register(PartnerInfo)
admin.site.register(ProductCategory)
admin.site.register(ProductDetails)
admin.site.register(CustomerInformation)
admin.site.register(TransactionDetails)
admin.site.register(Localities)
admin.site.register(Cities)