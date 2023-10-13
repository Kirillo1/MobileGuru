from django.shortcuts import render, redirect, get_object_or_404

from .models import SmartPhone, FulfilledSmartPhoneImages
from .forms import SmartPhoneForm

def view_index(request):
    smartphones = SmartPhone.objects.all()
    context = {
        'smartphones': smartphones,
        }
    return render(request, 'market/index.html', context)


def create_smartphone_view(request):
    if request.method == 'POST':
        form = SmartPhoneForm(request.POST)
        images= request.FILES.getlist('images')

        if form.is_valid():
            main_image = request.FILES.get('main_image')
            form.instance.main_image = main_image
            form.save()

            for image in images:
                photo = FulfilledSmartPhoneImages.objects.create(
                    smartphone=form.instance,
                    images=image
                )

            return redirect('market:index')
    else:
        form = SmartPhoneForm()

    return render(request, 'market/create_phone.html', {'form': form})


def detail_phone_view(request, smartphone_id):
    smartphone = get_object_or_404(SmartPhone, pk=smartphone_id)
    return render(request, 'market/detail_phone.html', {'smartphone': smartphone})