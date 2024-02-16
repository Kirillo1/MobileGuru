from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from marketapp.models import SmartPhone


def detail_company_view(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    smartphones = SmartPhone.objects.filter(seller=user)

    return render(request, 'companies/detail_company.html', {'company': user, 'smartphones': smartphones})
