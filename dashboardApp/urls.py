from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tables/', views.tables, name='tables'),
    path('charts/', views.charts, name='charts'),
    path('forms/', views.forms, name='forms'),
]

