from django.views.generic import ListView
from django.shortcuts import render

from dashboardApp.models import *
# Create your views here.


class Stores(ListView):
    model = Product
    template_name = 'store/store.html'


