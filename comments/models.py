from django.db import models
from django.contrib.auth import get_user_model

from marketapp.models import SmartPhone
from companies.models import Company


User = get_user_model()


class Comment(models.Model):
    smartphone = models.ForeignKey(
        SmartPhone,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Смартфон',
        blank=True,
        null=True,
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментарий',
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        User,
        related_name="comments",
        on_delete=models.CASCADE,
        verbose_name="Автор",
        null=True
    )
    content = models.TextField(
        "Контент",
        blank=False
    )
    created_at = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Дата изменения',
        auto_now=True
    )

    def __str__(self):
        return f"{self.content}. {self.author}"
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'