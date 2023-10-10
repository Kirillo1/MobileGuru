from django.urls import path
from .views import view_login, view_profile, view_logout

app_name = 'users'

urlpatterns = [
    path('login/', view_login, name='login'),
    path('profile/', view_profile, name='profile'),
    path('logout/', view_logout, name='logout'),
]

