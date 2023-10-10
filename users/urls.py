from django.urls import path
from .views import view_login

app_name = 'users'

urlpatterns = [
    path('login/', view_login, name='login')
]

