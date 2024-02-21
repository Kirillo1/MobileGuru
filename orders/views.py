from django.shortcuts import render

def view_basket(request):
    return render(request, 'orders/basket_detail.html')