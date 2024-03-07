from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import (Http404, HttpResponse, HttpResponseRedirect,
                         JsonResponse)

from comments.forms import CommentForm
from marketapp.models import SmartPhone
from companies.models import Company
from .models import Comment


@login_required
def create_comment_smarphone_view(request):
    if request.method != 'POST':
        raise Http404

    smartphone_id = request.POST.get('smartphone_id')
    text_comment = request.POST.get('text_comment')
    
    smartphone = SmartPhone.objects.get(id=smartphone_id)
    Comment.objects.create(
                        smartphone=smartphone,
                        author=request.user,
                        content=text_comment
                        )

    return JsonResponse({'status': 'ok'})


@login_required
def create_comment_company_view(request):
    if request.method != 'POST':
        raise Http404

    text_comment = request.POST.get('text_comment')
    title_hash = request.POST.get('title_hash')
    print(title_hash)
    
    company = Company.objects.get(title_hash=title_hash)
    Comment.objects.create(
                        company=company,
                        author=request.user,
                        content=text_comment
                        )

    return JsonResponse({'status': 'ok'})


@login_required
def delete_comment_view(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        try:
            comment = Comment.objects.get(pk=comment_id)
            smartphone_id = comment.smartphone.id
            comment.delete()
        except Comment.DoesNotExist:
            pass
    return HttpResponseRedirect(reverse('market:detail_phone', kwargs={'smartphone_id': smartphone_id}))


@login_required
def delete_comment_company_view(request, title_hash):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        try:
            comment = Comment.objects.get(pk=comment_id)
            comment.delete()
        except Comment.DoesNotExist:
            pass
    return HttpResponseRedirect(reverse('companies:detail_company', kwargs={'title_hash': title_hash}))


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
