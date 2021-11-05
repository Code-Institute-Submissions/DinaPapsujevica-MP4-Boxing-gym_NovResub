from django.urls import path
from . import views

urlpatterns = [
    path('fitnessplans/', views.select_subscription, name='fitnessplans'),
    path('subscribe/', views.create_stripe_subsription, name='subscribe'),
    path('checkout/', views.checkout_stripe_payment, name='checkout'),
    path('complete/', views.complete_shoping, name='complete'),
    path('thanks/', views.subscribe, name='thanks'),

]
