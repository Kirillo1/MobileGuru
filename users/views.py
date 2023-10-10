from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
# from .forms import UserLoginForm
from django.contrib import auth


def view_login(request: HttpRequest) -> HttpResponse:
    # if request.method == 'POST':
    #     form = UserLoginForm(data=request.POST)
    #     if form.is_valid():
    #         username = request.POST['username']
    #         password = request.POST['password']
    #         user = auth.authenticate(username=username, password=password)
    #         if user and user.is_active:
    #             auth.login(request, user)

    #             return HttpResponseRedirect(reverse('expert:index'))
    # else:
    #     form = UserLoginForm()

    # context = {
    #     'form': form
    # }

    return render(request, 'users/login.html')
