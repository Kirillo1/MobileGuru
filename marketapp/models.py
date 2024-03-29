from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from companies.models import Company

User = get_user_model()


class SmartPhone(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'На проверке'),
        ('Approved', 'Одобрено'),
        ('Rejected', 'Отклонено'),
    )
    brand = models.CharField(
        'Бренд', max_length=100
    )
    model = models.CharField(
        'Модель', max_length=100
    )
    display_size = models.DecimalField(
        'Размер экрана', max_digits=5,
        decimal_places=2
    )
    storage_capacity = models.PositiveIntegerField(
        'Объем встроенной памяти'
    )
    likes_count = models.PositiveIntegerField(
        default=0
    )
    seller = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name='Продавец',
        blank=True,
        null=True
    )
    processor = models.CharField(
        'Процессор', max_length=200
    )
    battery_capacity = models.PositiveIntegerField(
        'Объем батареи'
    )
    description = models.TextField(
        'Описание, характеристики'
    )
    created_at = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES,
        default='Pending'
    )
    main_image = models.ImageField(
        'Главное фото',
        upload_to='main_img/',
        null=True,
        blank=True
    )
    price = models.DecimalField(
        'Цена', max_digits=10, decimal_places=2
    )
    grade = models.DecimalField(
        'Оценка',
        max_digits=3,
        decimal_places=2,
        default=0.0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ]
    )
    
    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Смартфон'
        verbose_name_plural = 'Смартфоны'

    def like(self):
        self.likes_count += 1

    def unlike(self):
        if self.likes_count > 0:
            self.likes_count -= 1


class FulfilledSmartPhoneImages(models.Model):
    smartphone = models.ForeignKey(
        SmartPhone,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Смартфон',
    )

    images = models.ImageField(
        upload_to='SmartPhoneImages',
    )

    def __str__(self):
        return f'Фото к смартфону {self.smartphone.model}'

    class Meta:
        verbose_name = 'файл с фотографией к смартфону'
        verbose_name_plural = 'Фото к смартфонам'
