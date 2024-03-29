# Generated by Django 4.2.5 on 2024-03-19 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marketapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100, verbose_name='Регион')),
                ('area', models.CharField(max_length=100, verbose_name='Район')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('house', models.CharField(max_length=100, verbose_name='Дом')),
                ('apartment', models.CharField(max_length=100, verbose_name='Квартира')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderSmartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ')),
                ('smartphone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketapp.smartphone', verbose_name='Смартфон')),
            ],
            options={
                'verbose_name': 'Продукт в корзине',
                'verbose_name_plural': 'Продукты в корзине',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='smartphones',
            field=models.ManyToManyField(through='orders.OrderSmartphone', to='marketapp.smartphone', verbose_name='Смартфоны'),
        ),
    ]
