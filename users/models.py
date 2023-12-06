from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator



class User(AbstractUser):

    image = models.ImageField(
        'Ваш лого',
        upload_to='users_images',
        blank=True
    )
    phone_number = PhoneNumberField(
        'Номер телефона',
        unique=True
    )
    father_name = models.CharField(
        'Отчество',
        max_length=60,
        null=True,
        blank=True
    )
    company_name = models.CharField(
        'Название компании',
        max_length=100,
        null=True,
        blank=True
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

    company_information = models.TextField(
        'Информация о компани'
    )
