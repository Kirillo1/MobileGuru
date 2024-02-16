from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse

from .models import SmartPhone, FulfilledSmartPhoneImages
from comments.models import Comment
from users.models import User
from .forms import SmartPhoneForm, SmartPhoneEditForm


def view_index(request):
    smartphones = SmartPhone.objects.all()
    context = {
        'smartphones': smartphones,
    }
    return render(request, 'market/index.html', context)


@login_required
def create_smartphone_view(request):
    if request.method == 'POST':
        user = request.user
        form = SmartPhoneForm(request.POST)
        images = request.FILES.getlist('images')

        if form.is_valid():
            main_image = request.FILES.get('main_image')
            form.instance.main_image = main_image
            form.instance.seller = user
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
    comments = Comment.objects.filter(smartphone=smartphone_id)
    return render(request, 'market/detail_phone.html', 
                  {'smartphone': smartphone,
                   'comments': comments})


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


def is_moderator(user):
    return user.is_staff


@user_passes_test(is_moderator)
def moderator_list_view(request):
    pending_smartphones = SmartPhone.objects.all().filter(status="Pending")
    context = {
        'pending_smartphones': pending_smartphones,
    }
    return render(request, 'market/moderator_list.html', context)


def update_status_view(request, smartphone_id, new_status):
    try:
        smartphone = get_object_or_404(SmartPhone, pk=smartphone_id)
        smartphone.status = new_status
        smartphone.save()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False})


def like_smartphone(request, smartphone_id):
    smartphone = SmartPhone.objects.get(pk=smartphone_id)
    liked_cookie_name = f'liked_{smartphone_id}'

    if liked_cookie_name not in request.COOKIES:
        smartphone.likes_count += 1
        smartphone.save()
        response = JsonResponse({'likes': smartphone.likes_count})
        response.set_cookie(liked_cookie_name, '1')
        return response
    else:
        return JsonResponse({'error': 'Вы уже поставили лайк'})


def unlike_smartphone(request, smartphone_id):
    smartphone = SmartPhone.objects.get(pk=smartphone_id)
    liked_cookie_name = f'liked_{smartphone_id}'

    if liked_cookie_name in request.COOKIES:
        smartphone.likes_count -= 1
        smartphone.save()
        response = JsonResponse({'likes': smartphone.likes_count})
        response.delete_cookie(liked_cookie_name)
        return response
    else:
        return JsonResponse({'error': 'Вы еще не ставили лайк'})
