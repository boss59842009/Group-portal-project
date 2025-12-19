from django.db import models
from django.forms import Form, ChoiceField
from django.conf import settings

class Event(models.Model):
    
    title = models.CharField(max_length=100, verbose_name="Назва події")
    description = models.TextField(max_length=500, verbose_name="Опис")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="events")
    date_start = models.DateField(verbose_name="Дата початку")
    date_end = models.DateField(verbose_name="Дата завершення")
    time_start = models.TimeField(verbose_name="Час початку")
    time_end = models.TimeField(verbose_name="Час закінчення")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подія'
        verbose_name_plural = 'Події'
        ordering = ['-created_at']


