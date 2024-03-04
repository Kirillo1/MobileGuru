from django.urls import path

from .views import view_basket, add_to_basket, delete_product_basket, create_order_view

app_name = 'orders'

urlpatterns = [
    path("basket/", view_basket, name="view_basket"),
    path("add_to_basket/", add_to_basket, name="add_to_basket"),
    path("delete_basket/", delete_product_basket, name="delete_product_basket"),
    path("create_order/", create_order_view, name="create_order")
]