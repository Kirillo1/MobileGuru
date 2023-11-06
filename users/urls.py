from django.urls import path
from .views import (view_login, view_profile, view_logout, 
                    register_user, view_company)

app_name = 'users'

urlpatterns = [
    path('login/', view_login, name='login'),
    path('profile/', view_profile, name='profile'),
    path('logout/', view_logout, name='logout'),
    path('register/', register_user, name='register_user'),
    path('company/<int:user_id>/', view_company, name = 'company')
]
