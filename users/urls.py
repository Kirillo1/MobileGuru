from django.urls import path
from .views import (view_login, view_profile, view_logout, 
                    view_register_user)

app_name = 'users'

urlpatterns = [
    path('login/', view_login, name='login'),
    path('profile/', view_profile, name='profile'),
    path('logout/', view_logout, name='logout'),
    path('register/', view_register_user, name='register_user')
]
