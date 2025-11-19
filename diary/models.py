from django.db import models
from django.conf import settings

class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предмети"
        ordering = ['name']

class SchoolClass(models.Model):
    name = models.CharField(max_length=50, verbose_name="Назва класу")
    year = models.IntegerField(verbose_name="Рік навчання")
    letter = models.CharField(max_length=1, verbose_name="Літера класу")
    classroom_number = models.CharField(max_length=10, verbose_name="Номер кабінету")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")

    def __str__(self):
        return f"{self.name} - {self.letter} - {self.year}"
    
    class Meta:
        verbose_name = "Клас"
        verbose_name_plural = "Класи"
        ordering = ['name', 'letter']

class Grade(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Учень")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades', verbose_name="Предмет")
    score = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Оцінка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.score}"
    
    class Meta:
        verbose_name = "Оцінка"
        verbose_name_plural = "Оцінки"
        ordering = ['-created_at']