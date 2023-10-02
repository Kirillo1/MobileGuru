from django.urls import path

from marketapp.views import (view_index,)

app_name = 'market'

urlpatterns = [
    path('', view_index, name='index')
]