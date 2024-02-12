from django.shortcuts import render, redirect

from comments.forms import CommentForm
from marketapp.models import SmartPhone
from users.models import User


def create_comment_view(request, pk):
    smartphone = SmartPhone.objects.get(pk=pk)

    if request.method == 'POST':
        user = request.user
        form = CommentForm(request.POST)

        if form.is_valid():
            form.instance.smartphone = smartphone
            form.instance.author = user
            form.save()

            return redirect('market:index')
    else:
        form = CommentForm()
        
    return render(request, 'comments/create_view.html', {'form': form})
