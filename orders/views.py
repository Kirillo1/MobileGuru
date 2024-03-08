import json

from django.shortcuts import render, reverse
from django.http import (Http404, HttpResponse, HttpRequest,
                         HttpResponseRedirect, JsonResponse)

from marketapp.models import SmartPhone
from .models import Basket


def view_basket(request: HttpRequest) -> HttpResponse:
    baskets = Basket.objects.filter(user_name=request.user)
    return render(request, 'orders/basket_detail.html', context={
        'baskets': baskets
    })


def add_to_basket(request: HttpRequest) -> JsonResponse:
    if request.method != 'POST':
        raise Http404

    smartphone_id = request.POST.get('smartphone_id')
    quantity = request.POST.get('productQuantity')
    smartphone: SmartPhone = SmartPhone.objects.get(id=smartphone_id)
    user = request.user

    Basket.objects.create(user_name=user,
                          smartphone=smartphone,
                          quantity=quantity
                          )

    return JsonResponse({'status': 'ok'})


def delete_product_basket(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        basket_id = request.POST.get('basket_id')

        try:
            basket: Basket = Basket.objects.get(pk=basket_id)
            basket.delete()
        except Basket.DoesNotExist:
            pass

    return HttpResponseRedirect(reverse('orders:view_basket'))


def view_order_create(request: HttpRequest) -> JsonResponse:
    basket: Basket = Basket.objects.filter(user_name=request.user)

    if request.method == 'POST':
        data = json.loads(request.body)

        region = data.get('region')
        area = data.get('area')
        city = data.get('city')
        street = data.get('street')
        house = data.get('house')
        apartment = data.get('apartment')

        return JsonResponse({'status': 'ok', 'data_received': data})

    return JsonResponse({'error': 'Method not allowed'}, status=405)
