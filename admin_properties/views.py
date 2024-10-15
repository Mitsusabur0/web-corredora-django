from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Property
from .forms import PropertyForm
# Create your views here.



class PropertyListView(ListView):
    model = Property
    template_name = 'admin_properties/admin_property_list.html'
    context_object_name = 'properties'  



class PropertyCreateView(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'admin_properties/property_form.html'
    success_url = reverse_lazy('a_properties_list')