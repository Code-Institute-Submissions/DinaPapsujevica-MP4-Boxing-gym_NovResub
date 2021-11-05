from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('trial/', views.trial, name='trial'),
    path('classes/', views.classes, name='classes')
]
