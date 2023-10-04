from django import forms
from .models import SmartPhone, FulfilledSmartPhoneImages

class SmartPhoneForm(forms.ModelForm):
    brand = forms.CharField(
        label='Бренд',
        widget=forms.TextInput(attrs={'placeholder': 'Бренд'}),
        required=True
    )
    
    model = forms.CharField(
        label='Модель',
        widget=forms.TextInput(attrs={'placeholder': 'Модель'}),
        required=True
    )

    display_size = forms.DecimalField(
        label='Размер экрана',
        widget=forms.NumberInput(attrs={'placeholder': 'Размер экрана'}),
        required=True
    )

    storage_capacity = forms.IntegerField(
        label='Объем встроенной памяти',
        widget=forms.NumberInput(attrs={'placeholder': 'Объем встроенной памяти'}),
        required=True
    )

    processor = forms.CharField(
        label='Процессор',
        widget=forms.TextInput(attrs={'placeholder': 'Процессор'}),
        required=True
    )

    battery_capacity = forms.IntegerField(
        label='Объем батареи',
        widget=forms.NumberInput(attrs={'placeholder': 'Объем батареи'}),
        required=True
    )

    description = forms.Textarea()

    price = forms.DecimalField(
        label='Цена',
        widget=forms.NumberInput(attrs={'placeholder': 'Цена'}),
        required=True
    )

    class Meta:
        model = SmartPhone
        fields = ('brand', 'model', 'display_size', 'storage_capacity', 'processor', 
                  'battery_capacity', 'description', 'price')

class SmartPhoneImagesForm(forms.ModelForm):
    # images = forms.ImageField(
    # widget=forms.ImageField(attrs={'multiple': True, 'images': 'image[]'}),
    # required=False
    # )

    class Meta:
        model = FulfilledSmartPhoneImages
        fields = ('image',)
