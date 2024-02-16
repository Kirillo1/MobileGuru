from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login
from .models import Company
from .forms import CompanyRegistrationForm
from marketapp.models import SmartPhone


def detail_company_view(request, user_id):
    user = get_object_or_404(Company, pk=user_id)
    smartphones = SmartPhone.objects.filter(seller=user)

    return render(request, 'companies/detail_company.html', {'company': user, 'smartphones': smartphones})


def register_company_view(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            main_image = request.FILES.get('main_image')
            form.instance.image = main_image
            user = form.save()
            login(request, user)
            return redirect('market:index')
        else:
            for field, errors in form.errors.items():
                print(f"Field: {field}, Errors: {', '.join(errors)}")
    else:
        form = CompanyRegistrationForm()
    return render(request, 'companies/register_company.html', {'form': form})