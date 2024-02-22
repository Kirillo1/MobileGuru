from django.urls import path

from .views import view_basket, add_to_basket

app_name = 'orders'

urlpatterns = [
    path("basket/", view_basket, name="view_basket"),
    path("add_to_basket/", add_to_basket, name="add_to_basket")
]