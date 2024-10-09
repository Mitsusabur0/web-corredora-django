from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core/urls')),
    path('properties/', include('front_properties/urls'), namespace='properties'),
    path('a/clients/', include('admin_clients/urls'), namespace='admin_clients'),
    path('a/properties/', include('admin_properties/urls'), namespace='admin_properties'),
    path('a/managements/', include('admin_managements/urls'),  namespace='admin_managements'),
    
]
