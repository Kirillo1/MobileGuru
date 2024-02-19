from django.contrib import admin

from .models import Order, OrderSmartphone, Basket

admin.site.register(Order)
admin.site.register(OrderSmartphone)
admin.site.register(Basket)
