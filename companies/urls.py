from django.urls import path
from .views import detail_company_view, register_company_view


app_name = 'companies'

urlpatterns = [
    path('detail_company/<str:title_hash>/', detail_company_view, name = 'detail_company'),
    path('register_company/', register_company_view, name = 'register_company')
]
