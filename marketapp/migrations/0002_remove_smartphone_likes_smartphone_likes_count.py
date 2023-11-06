# Generated by Django 4.2.5 on 2023-10-21 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='likes',
        ),
        migrations.AddField(
            model_name='smartphone',
            name='likes_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
