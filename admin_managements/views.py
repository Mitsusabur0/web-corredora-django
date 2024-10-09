from django.shortcuts import render

# Create your views here.


def managements(request):
    return render(request, 'admin_managements/managements_list.html')