from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients, name='a_clients_list'),
    # path('examples/', views.examples, name='examples'),
]