from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


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

    # rating =

    # company_information =
