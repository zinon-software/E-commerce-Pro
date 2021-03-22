from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', Stores.as_view(), name='stores'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),

]
