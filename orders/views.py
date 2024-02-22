from django.shortcuts import render
from django.http import (Http404, HttpResponse, HttpResponseRedirect,
                         JsonResponse)

def view_basket(request):
    return render(request, 'orders/basket_detail.html')



def add_to_basket(request):
    if request.method != 'POST':
        raise Http404

    smartphone_id = request.POST.get('smartphone_id')
    status = request.POST.get('status')
    print(smartphone_id)
        
    return JsonResponse({'status': 'ok'})
