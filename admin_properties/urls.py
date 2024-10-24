from django.urls import path
from .views import PropertyCreateView, PropertyManagementView, PropertyUpdateView, PropertyDeleteView

urlpatterns = [
    # path('', PropertyListView.as_view(), name='a_properties_list'),
    path('add/', PropertyCreateView.as_view(), name='property_add'),
    path('management/', PropertyManagementView.as_view(), name='property_management'),
    path('add/', PropertyCreateView.as_view(), name='property_add'),
    path('<int:pk>/edit/', PropertyUpdateView.as_view(), name='property_edit'),
    path('<int:pk>/delete/', PropertyDeleteView.as_view(), name='property_delete'),
]



