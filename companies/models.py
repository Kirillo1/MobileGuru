from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User


class Company(models.Model):
    email = models.EmailField(
        'Электронная почта компании'
    )
    phonenumber = PhoneNumberField(
        'Номер телефона компании'
    )
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='owner',
        verbose_name='Владелец'
    )
    image = models.ImageField(
        'Ваш лого',
        upload_to='users_images',
        blank=True
    )
    phone_number = PhoneNumberField(
        'Номер телефона',
        unique=True
    )
    company_name = models.CharField(
        'Название компании',
        max_length=100,
        null=True,
        blank=True
    )
    title_hash = models.CharField(
        'Хеш названия компании',
        max_length=150,
        blank=True,
        null=True
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

    def save(self, *args, **kwargs):
        if not self.title_hash:
            self.title_hash = abs(hash(self.company_name))

        super().save(*args, **kwargs)
