from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from marketapp.models import SmartPhone


User = get_user_model()


class Order(models.Model):
    user_name = models.ForeignKey(
        User, related_name="orders", 
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )

    region = models.CharField(
        'Регион',
        max_length=100, 
    )
    area = models.CharField(
        'Район',
        max_length=100, 
    )
    city = models.CharField(
        'Город',
        max_length=100, 
    )
    house = models.CharField(
        'Дом',
        max_length=100, 
    )
    apartment = models.CharField(
        'Квартира',
        max_length=100, 
    )
    date_of_creation = models.DateTimeField(
        'Дата создания', 
        auto_now_add=True
    )
    smartphones = models.ManyToManyField(
        SmartPhone, 
        verbose_name="Смартфоны",
        through='orders.OrderSmartphone', 
        through_fields=['order', 'smartphone']
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderSmartphone(models.Model):
    smartphone = models.ForeignKey(
        SmartPhone, 
        on_delete=models.CASCADE,
        verbose_name='Смартфон'
    )
    order = models.ForeignKey(
        Order, 
        verbose_name='Заказ', 
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Количество", 
        default=1
    )

    def __str__(self):
        return f'{self.smartphone} - {self.quantity}'

    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзине'


class Basket(models.Model):
    user_name = models.ForeignKey(
        User, related_name="basket", 
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    smartphone = models.ForeignKey(
        SmartPhone, 
        on_delete=models.CASCADE,
        verbose_name="Смартфон"
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Количество", 
        default=1
    )

    def get_product_total(self):
        return self.quantity * self.smartphone.price

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

