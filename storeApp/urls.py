from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', Stores.as_view(), name='stores'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),

    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),

]
