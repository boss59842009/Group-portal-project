from django.db import models
from django.conf import settings

class Thread(models.Model):
    name = models.CharField(max_length=40, verbose_name="Назва треду")

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="threads")
    
    description = models.TextField(max_length=555, verbose_name="Опис треду")
    icon = models.ImageField(upload_to="threads/icons", verbose_name="Картинка", blank="True", null="True")


    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редагування")

class Messages(models.Model):
    text = models.TextField(max_length=255, verbose_name="Текст повідомлення")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="messages")
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="messages")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редагування")
