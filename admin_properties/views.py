from django.shortcuts import render

# Create your views here.
def properties(request):
    return render(request, 'admin_properties/admin_property_list.html')