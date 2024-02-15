from django.urls import path
from .views import (create_comment_view, delete_comment_view)

app_name = 'comments'

urlpatterns = [
    path('create_comment/<int:pk>', create_comment_view, name='create_comment'),
    path('delete_comment/<int:pk>', delete_comment_view, name='delete_comment'),
]