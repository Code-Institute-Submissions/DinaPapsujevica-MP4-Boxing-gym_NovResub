from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('trial/', views.trial, name='trial'),
    path('classes/', views.classes, name='classes'),
    path('fitnessplans/', views.select_subscription, name='fitnessplans'),
    path('checkout/', views.create_stripe_subsription, name='checkout'),
    path('addproduct/', views.add_product, name='add_product'),
]
