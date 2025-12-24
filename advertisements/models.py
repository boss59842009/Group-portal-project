from django.db import models
from django.utils import timezone
from auth_system.models import CustomUser


# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст оголошення")
    media = models.FileField(upload_to='advertisements/', blank=True, null=True, verbose_name="Файл (картинка, відео або документ)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Останнє оновлення")
    expiration_date = models.DateField(blank=True, null=True, verbose_name="Дата закінчення")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Автор")
    is_active = models.BooleanField(default=True, verbose_name="Активне")

    class Meta:
        verbose_name = "Оголошення"
        verbose_name_plural = "Оголошення"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def is_expired(self):
        if self.expiration_date:
            return timezone.now().date() > self.expiration_date
        return False
