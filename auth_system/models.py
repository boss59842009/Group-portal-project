from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Адміністратор'),
        ('moderator', 'Модератор'),
        ('user', 'Користувач'),
    ]

    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Дата народження")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="Аватар")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user', verbose_name="Роль")
    bio = models.TextField(blank=True, verbose_name="Про себе")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"

    def __str__(self):
        return self.username

    def can_manage_advertisements(self):
        return self.role in ['admin', 'moderator']
