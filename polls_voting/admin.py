from django.contrib import admin
from .models import Survey, Question, Choice, SurveyResult, Answer
from .models import Voting, VotingOption, Vote

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "is_active", "multi_step")
    list_filter = ("is_active", "multi_step")
    search_fields = ("title",)
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "survey")
    search_fields = ("text",)
    inlines = [ChoiceInline]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("text", "question")
    search_fields = ("text",)


@admin.register(SurveyResult)
class SurveyResultAdmin(admin.ModelAdmin):
    list_display = ("user", "survey", "submitted_at")
    list_filter = ("survey", "submitted_at")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("result", "question", "choice")

###

class VotingOptionInline(admin.TabularInline):
    model = VotingOption
    extra = 1


@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title",)
    inlines = [VotingOptionInline]


@admin.register(VotingOption)
class VotingOptionAdmin(admin.ModelAdmin):
    list_display = ("text", "voting")


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("user", "voting", "option", "updated_at")
    list_filter = ("voting",)