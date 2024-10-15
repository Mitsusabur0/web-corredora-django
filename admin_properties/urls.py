from django.urls import path
from .views import PropertyListView, PropertyCreateView

urlpatterns = [
    path('', PropertyListView.as_view(), name='a_properties_list'),
    path('add/', PropertyCreateView.as_view(), name='property_add'),
]