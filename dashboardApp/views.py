from django.shortcuts import render

# Create your views here.

def dashboard(request):

    return render(request, 'dashboard/index.html')


def tables(request):

    return render(request, 'dashboard/tables.html')

def charts(request):

    return render(request, 'dashboard/charts.html')


def forms(request):

    return render(request, 'dashboard/forms.html')