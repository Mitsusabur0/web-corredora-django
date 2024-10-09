from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    # path('properties/', include('front_properties.urls')),
    path('a/clients/', include('admin_clients.urls')),
    # path('a/properties/', include('admin_properties.urls')),
    # path('a/managements/', include('admin_managements.urls')),
    
]
