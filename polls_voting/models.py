from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Survey(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва")
    description = models.TextField(blank=True, verbose_name="Опис")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name="Активне")
    multi_step = models.BooleanField(default=False, verbose_name="Закрите")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name="authors", verbose_name="Автор")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Опитування'
        verbose_name_plural = 'Опитування'


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="questions", verbose_name="Питання")
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Питання'
        verbose_name_plural = 'Питання'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices", verbose_name="Вибір")
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вибір'
        verbose_name_plural = 'Вибори'


class SurveyResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name="users", verbose_name="Користувач")
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "survey")

    def __str__(self):
        return f"{self.user} - {self.survey}"


class Answer(models.Model):
    result = models.ForeignKey(SurveyResult, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="answers",
                               verbose_name="Автор")

    class Meta:
        verbose_name = 'Відповідь'
        verbose_name_plural = 'Відповіді'

###

class Voting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="votings",
                               verbose_name="Автор")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Голосування'
        verbose_name_plural = 'Голосування'


class VotingOption(models.Model):
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE, related_name="options")
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name="user", verbose_name="Користувач")
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE)
    option = models.ForeignKey(VotingOption, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "voting")



