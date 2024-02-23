from django.shortcuts import render
from django.http import (Http404, HttpResponse, HttpResponseRedirect,
                         JsonResponse)
from marketapp.models import SmartPhone
from .models import Basket

def view_basket(request):
    baskets = Basket.objects.filter(user_name=request.user)
    return render(request, 'orders/basket_detail.html', context={
        'baskets': baskets
    })


def add_to_basket(request):
    if request.method != 'POST':
        raise Http404

    smartphone_id = request.POST.get('smartphone_id')
    quantity = request.POST.get('productQuantity')
    smartphone = SmartPhone.objects.get(id=smartphone_id)
    user = request.user
    new_basket = Basket.objects.create(user_name=user,
                                    smartphone=smartphone,
                                    quantity=quantity
                                    )
    print(new_basket.id)
    print(quantity)

    return JsonResponse({'status': 'ok'})
