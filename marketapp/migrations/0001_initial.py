# Generated by Django 4.2.5 on 2024-02-16 18:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FulfilledSmartPhoneImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='SmartPhoneImages')),
            ],
            options={
                'verbose_name': 'файл с фотографией к смартфону',
                'verbose_name_plural': 'Фото к смартфонам',
            },
        ),
        migrations.CreateModel(
            name='SmartPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100, verbose_name='Бренд')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('display_size', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Размер экрана')),
                ('storage_capacity', models.PositiveIntegerField(verbose_name='Объем встроенной памяти')),
                ('likes_count', models.PositiveIntegerField(default=0)),
                ('processor', models.CharField(max_length=200, verbose_name='Процессор')),
                ('battery_capacity', models.PositiveIntegerField(verbose_name='Объем батареи')),
                ('description', models.TextField(verbose_name='Описание, характеристики')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('status', models.CharField(choices=[('Pending', 'На проверке'), ('Approved', 'Одобрено'), ('Rejected', 'Отклонено')], default='Pending', max_length=20)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='main_img/', verbose_name='Главное фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('grade', models.DecimalField(decimal_places=2, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
            ],
            options={
                'verbose_name': 'Смартфон',
                'verbose_name_plural': 'Смартфоны',
            },
        ),
    ]