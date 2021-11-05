from django.urls import path
from . import views

urlpatterns = [
    path('add_to_bag/<int:product_id>', views.add_to_bag, name='add_to_bag'),
    path('bags/', views.view_shopping_bag, name='bags'),
    path('adjust_bag/', views.update_bag, name='adjust_bag'),
    path('delete_item/<int:pid>', views.delete_from_shopping_bag, name='delete_item'),

]
