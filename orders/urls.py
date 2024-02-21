from django.urls import path

from .views import view_basket

app_name = 'orders'

urlpatterns = [
    path("basket/", view_basket, name="view_basket")
]