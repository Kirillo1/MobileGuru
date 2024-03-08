from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import (HttpResponseRedirect, HttpRequest, 
                         HttpResponse)
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import logout, login

from .forms import (UserProfileForm, UserLoginForm, 
                    AvatarUserForm, UserRegistrationForm)


def view_login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)

                return HttpResponseRedirect(reverse('market:index'))
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }

    return render(request, 'users/login.html', context)


@login_required(login_url='users:login')
def view_profile(request: HttpRequest) -> HttpResponse:
    user = request.user
    if request.method == 'POST':
        avatar_form = AvatarUserForm(
            request.POST, request.FILES, instance=request.user)
        form = UserProfileForm(data=request.POST, instance=user)
        if form.is_valid():
            avatar_form.save()
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=user)
        avatar_form = AvatarUserForm(instance=user)

    context = {
        'form': form,
        'groups': [group.name for group in user.groups.all()],
        'avatar_form': avatar_form,
    }

    return render(request, 'users/profile.html', context=context)


def view_logout(request: HttpRequest) -> HttpResponse:
    logout(request)

    return HttpResponseRedirect(reverse('market:index'))


def view_register_user(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            main_image = request.FILES.get('main_image')
            form.instance.image = main_image
            user = form.save()
            login(request, user)
            return redirect('companies:register_company')

    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})
