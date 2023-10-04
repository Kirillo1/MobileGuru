from django.urls import path

from marketapp.views import (view_index, create_smartphone)

app_name = 'market'

urlpatterns = [
    path('', view_index, name='index'),
    path('create_smartphone/', create_smartphone, name='create_smartphone'),
]