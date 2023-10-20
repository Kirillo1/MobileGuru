from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import SmartPhone, FulfilledSmartPhoneImages
from users.models import User
from .forms import SmartPhoneForm, SmartPhoneEditForm

def view_index(request):
    smartphones = SmartPhone.objects.all()
    all_users = User.objects.filter(is_staff=False)
    context = {
        'smartphones': smartphones,
        'all_users': all_users
        }
    return render(request, 'market/index.html', context)

@login_required
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


@login_required
def delete_smartphone_view(request, smartphone_id):
    smartphone = get_object_or_404(SmartPhone, pk=smartphone_id)

    if request.method == 'POST':
        smartphone.delete()
        return redirect('market:index')
    return render(request, 'market/delete_phone.html', {'smartphone': smartphone})


@login_required
def edit_smartphone_view(request, smartphone_id):
    smartphone = SmartPhone.objects.get(pk=smartphone_id)

    if request.method == 'POST':
        form = SmartPhoneEditForm(request.POST, instance=smartphone)

        if form.is_valid():
            form.save()
            return redirect('market:index')
    else:
        form = SmartPhoneEditForm(instance=smartphone)

    return render(request, 'market/edit_phone.html', {'form': form, 'smartphone': smartphone})