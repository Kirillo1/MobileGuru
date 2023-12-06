from django import forms
from .models import SmartPhone


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
        widget=forms.NumberInput(
            attrs={'placeholder': 'Объем встроенной памяти'}),
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

    def __init__(self, *args, **kwargs):
        super(SmartPhoneForm, self).__init__(*args, **kwargs)

        self.fields['brand'].widget.attrs['class'] = 'form-control'
        self.fields['model'].widget.attrs['class'] = 'form-control'
        self.fields['display_size'].widget.attrs['class'] = 'form-control'
        self.fields['storage_capacity'].widget.attrs['class'] = 'form-control'
        self.fields['processor'].widget.attrs['class'] = 'form-control'
        self.fields['battery_capacity'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'


class SmartPhoneEditForm(SmartPhoneForm):
    class Meta:
        model = SmartPhone
        fields = ['brand', 'model', 'display_size', 'storage_capacity', 'processor',
                  'battery_capacity', 'description', 'price']
