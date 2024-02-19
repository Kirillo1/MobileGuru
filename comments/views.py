from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from comments.forms import CommentForm
from marketapp.models import SmartPhone
from companies.models import Company
from .models import Comment


@login_required
def create_comment_smarphone_view(request, pk):
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


@login_required
def create_comment_company_view(request, title_hash):
    company = Company.objects.get(title_hash=title_hash)

    if request.method == 'POST':
        user = request.user
        form = CommentForm(request.POST)

        if form.is_valid():
            form.instance.company = company
            form.instance.author = user
            form.save()

            return redirect('market:index')
    else:
        form = CommentForm()
        
    return render(request, 'comments/create_view.html', {'form': form})


@login_required
def delete_comment_view(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('market:index')
    
    return render(request, 'comments/delete_view.html', {'comment': comment})


@login_required
def edit_comment_view(request, pk):
    comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            form.save()
            return redirect('market:index')
    else:
        form = CommentForm(instance=comment)

    return render(request, 'comments/edit_view.html', {'form': form, 'comment': comment})