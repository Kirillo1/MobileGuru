from django.urls import path
from .views import detail_company_view


app_name = 'companies'

urlpatterns = [
    path('company/<int:user_id>/', detail_company_view, name = 'company')
]
