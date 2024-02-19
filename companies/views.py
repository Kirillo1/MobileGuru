from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Company
from .forms import CompanyRegistrationForm
from marketapp.models import SmartPhone
from comments.models import Comment
from users.models import User



def detail_company_view(request, title_hash):
    company = get_object_or_404(Company, title_hash=title_hash)
    company_owner =  User.objects.get(username=company.owner)
    smartphones = SmartPhone.objects.filter(seller=company)
    comments = Comment.objects.filter(company=company)

    return render(request, 'companies/detail_company.html', 
                  {'company': company,
                    'company_owner': company_owner,
                    'smartphones': smartphones,
                    'comments': comments})


def register_company_view(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)

        if form.is_valid():
            main_image = request.FILES.get('main_image')
            form.instance.owner = request.user
            form.instance.image = main_image
            form.save()

            return redirect('market:index')
    else:
        form = CompanyRegistrationForm()

    return render(request, 'companies/register_company.html', {'form': form})