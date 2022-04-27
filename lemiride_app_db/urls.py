from django.urls import path
from .views import CustomerInformationViews

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer-information/', CustomerInformationViews.as_view())
]