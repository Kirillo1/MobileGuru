from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(
        'Адрес электронной почты',
        unique=True
    )
    phonenumber = PhoneNumberField(
        'Номер телефона',
        unique=True,
    )
    father_name = models.CharField(
        'Отчество',
        max_length=50,
        blank=True,
        null=True
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phonenumber']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
