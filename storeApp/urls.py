from django.urls import path
from .views import *

urlpatterns = [
    path('', Stores.as_view(), name='stores'),

]
