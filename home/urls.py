from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('trial/', views.trial, name='trial'),
    path('classes/', views.classes, name='classes'),
    path('fitnessplans/', views.select_subscription, name='fitnessplans'),
    path('subscribe/', views.create_stripe_subsription, name='subscribe'),
    path('addproduct/', views.add_product, name='add_product'),
    path('products/', views.view_products, name='products'),
    path('product_detail/<int:product_id>', views.product_detail, name='product_detail'),
    path('edit_product/<int:product_id>', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>', views.delete_product, name='delete_product'),
]
