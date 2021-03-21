from django.urls import path
from . import views

urlpatterns = [
    path('', views.stores, name='stores'),

]
