# Generated by Django 4.2.5 on 2023-12-03 16:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0002_remove_smartphone_likes_smartphone_likes_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone',
            name='grade',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка'),
        ),
    ]