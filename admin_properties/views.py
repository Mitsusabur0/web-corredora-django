from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Property
from .forms import PropertyForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin




class PropertyManagementView(LoginRequiredMixin, ListView):
    model = Property
    template_name = 'admin_properties/property_management.html'
    context_object_name = 'properties'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Property.objects.all().order_by('-date_published')
        
        # Search functionality
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(address__icontains=search_query) |
                Q(property_description__icontains=search_query)
            )
            
        # Filter by property type
        property_type = self.request.GET.get('property_type')
        if property_type:
            queryset = queryset.filter(property_type=property_type)
            
        # Filter by offer type
        offer_type = self.request.GET.get('offer_type')
        if offer_type:
            queryset = queryset.filter(offer_type=offer_type)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['property_types'] = Property.PROPERTY_TYPES
        context['offer_types'] = Property.OFFER_TYPE
        
        # Preserve GET parameters for pagination
        context['current_filters'] = self.request.GET.copy()
        if 'page' in context['current_filters']:
            del context['current_filters']['page']
            
        return context
    





class PropertyCreateView(LoginRequiredMixin, CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'admin_properties/property_form.html'
    success_url = reverse_lazy('property_management')

    def form_valid(self, form):
        messages.success(self.request, 'Property created successfully!')
        return super().form_valid(form)

class PropertyUpdateView(LoginRequiredMixin, UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = 'admin_properties/property_form.html'
    success_url = reverse_lazy('property_management')

    def form_valid(self, form):
        messages.success(self.request, 'Property updated successfully!')
        return super().form_valid(form)

class PropertyDeleteView(LoginRequiredMixin, DeleteView):
    model = Property
    template_name = 'admin_properties/property_confirm_delete.html'
    success_url = reverse_lazy('property_management')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Property deleted successfully!')
        return super().delete(request, *args, **kwargs)


    

# class PropertyListView(ListView):
#     model = Property
#     template_name = 'admin_properties/admin_property_list.html'
#     context_object_name = 'properties'  



# class PropertyCreateView(CreateView):
#     model = Property
#     form_class = PropertyForm
#     template_name = 'admin_properties/property_form.html'
#     success_url = reverse_lazy('a_properties_list')