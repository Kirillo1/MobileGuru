from django.shortcuts import render, redirect

from .models import SmartPhone, FulfilledSmartPhoneImages
from .forms import SmartPhoneForm

def view_index(request):
    smartphones = SmartPhone.objects.all()
    context = {'smartphones': smartphones}
    return render(request, 'market/index.html', context)


def create_smartphone(request):
    if request.method == 'POST':
        form = SmartPhoneForm(request.POST, request.FILES)
        if form.is_valid():
            smartphone = form.save()
    else:
        form = SmartPhoneForm()
    
    return render(request, 'market/create_phone.html', {'form': form})