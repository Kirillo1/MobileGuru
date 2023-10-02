from django.shortcuts import render

from .models import SmartPhone, FulfilledSmartPhoneImages

def view_index(request):
    smartphones = SmartPhone.objects.all()
    context = {'smartphones': smartphones}
    return render(request, 'market/index.html', context)
