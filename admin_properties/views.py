from django.shortcuts import render
from django.views.generic import ListView
from .models import Property

# Create your views here.



class PropertyListView(ListView):
    model = Property
    template_name = 'admin_properties/admin_property_list.html'
    context_object_name = 'properties'  