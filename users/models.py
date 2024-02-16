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
    phone_number = PhoneNumberField(
        'Номер телефона',
        unique=True,
    )
    father_name = models.CharField(
        'Отчество',
        max_length=50,
        blank=True,
        null=True
    )
    image = models.ImageField(
        'Ваша фотография',
        upload_to='users_images',
        blank=True
    )
    
    groups_user = models.ManyToManyField('auth.Group', related_name='user_set_custom')


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
