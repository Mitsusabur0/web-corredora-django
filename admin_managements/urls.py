from django.urls import path
from . import views

urlpatterns = [
    path('', views.managements, name='a_managements_list'),
    
]