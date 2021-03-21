from django.shortcuts import render

# Create your views here.

def stores(request):
    return render(request, 'dashboard/tables.html')
