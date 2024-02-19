from django.urls import path
from .views import (create_comment_smarphone_view, delete_comment_view, edit_comment_view,
                    create_comment_company_view)

app_name = 'comments'

urlpatterns = [
    path('create_comment/<int:pk>', create_comment_smarphone_view, name='create_comment'),
    path('create_comment_company/<str:title_hash>', create_comment_company_view, name='create_comment_company'),
    path('delete_comment/<int:pk>', delete_comment_view, name='delete_comment'),
    path('edit_comment/<int:pk>', edit_comment_view, name='edit_comment')
]