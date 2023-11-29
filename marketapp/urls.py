from django.urls import path

from marketapp.views import (view_index, create_smartphone_view, detail_phone_view,
                             delete_smartphone_view, edit_smartphone_view,
                             like_smartphone, unlike_smartphone, moderator_list_view,
                             update_status_view)

app_name = 'market'

urlpatterns = [
    path('', view_index, name='index'),
    path('create_smartphone/', create_smartphone_view, name='create_smartphone'),
    path('smartphone/<int:smartphone_id>/', detail_phone_view, name='detail_phone'),
    path('smartphone/<int:smartphone_id>/delete/', delete_smartphone_view, name='smartphone_delete'),
    path('smartphone/<int:smartphone_id>/edit/', edit_smartphone_view, name='smartphone_edit'),
    path('like_smartphone/<int:smartphone_id>/', like_smartphone, name='like_smartphone'),
    path('unlike_smartphone/<int:smartphone_id>/', unlike_smartphone, name='unlike_smartphone'),
    path('moderator/', moderator_list_view, name='moderator_list'),
    path('update_status/<int:smartphone_id>/<str:new_status>/', update_status_view, name='update_status')
]