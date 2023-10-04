from django.shortcuts import render, redirect

from .models import SmartPhone, FulfilledSmartPhoneImages
from .forms import SmartPhoneForm, SmartPhoneImagesForm

def view_index(request):
    smartphones = SmartPhone.objects.all()
    context = {'smartphones': smartphones}
    return render(request, 'market/index.html', context)


def create_smartphone(request):
    if request.method == 'POST':
        form = SmartPhoneForm(request.POST)
        images_form = SmartPhoneImagesForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid() and images_form.is_valid():
            smartphone = form.save(commit=False)
            smartphone.save()

            images = images_form.save(commit=False)
            images.smartphone = smartphone
            images.save()

            return redirect('market:index')
    else:
        form = SmartPhoneForm()
        images_form = SmartPhoneImagesForm()

    return render(request, 'market/create_phone.html', {'form': form, 'images_form': images_form})