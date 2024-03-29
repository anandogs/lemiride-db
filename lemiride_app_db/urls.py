from django.urls import path
from .views import CustomerInformationViews, LocalitiesViews, ProductDetailsViews, UserViews, TransactionCreate

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer-information/', CustomerInformationViews.as_view()),
    path('customer-information/<str:number>', CustomerInformationViews.as_view()),
    path('localities/', LocalitiesViews.as_view()),
    path('product-details/', ProductDetailsViews.as_view()),
    path('product-details/<str:location>-<str:city>-<int:day>-<int:month>-<int:year>-<int:hour>-<int:minute>', ProductDetailsViews.as_view()),
    path('user/', UserViews.as_view()),
    path('transaction-create/', TransactionCreate.as_view()),
]
