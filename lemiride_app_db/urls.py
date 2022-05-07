from django.urls import path
from .views import CustomerInformationViews, LocalitiesViews

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer-information/', CustomerInformationViews.as_view()),
    path('localities/', LocalitiesViews.as_view())
]