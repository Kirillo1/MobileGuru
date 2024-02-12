from django.urls import path
from .views import (create_comment_view,)

app_name = 'comments'

urlpatterns = [
    path('create_comment/<int:pk>', create_comment_view, name='create_comment'),
]