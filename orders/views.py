import json
from django.shortcuts import render, reverse
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
    Basket.objects.create(user_name=user,
                        smartphone=smartphone,
                        quantity=quantity
                        )

    return JsonResponse({'status': 'ok'})


def delete_product_basket(request):
    if request.method == 'POST':
        basket_id = request.POST.get('basket_id')
        try:
            basket = Basket.objects.get(pk=basket_id)
            basket.delete()
        except Basket.DoesNotExist:
            pass
    return HttpResponseRedirect(reverse('orders:view_basket'))


def create_order_view(request):
    basket = Basket.objects.filter(user_name=request.user)
    print(basket)

    if request.method == 'POST':
        data = json.loads(request.body)
        
        region = data.get('region')
        area = data.get('area')
        city = data.get('city')
        street = data.get('street')
        house = data.get('house')
        apartment = data.get('apartment')
        print(region)
        print(area)
        print(city)
        print(street)
        print(house)
        print(apartment)

        
        
        return JsonResponse({'status': 'ok', 'data_received': data})
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

