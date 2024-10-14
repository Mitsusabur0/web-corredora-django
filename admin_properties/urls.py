from django.urls import path
from .views import PropertyListView

urlpatterns = [
    path('', PropertyListView.as_view(), name='a_properties_list'),
]