from django.shortcuts import render
from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView

from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Survey, Question, Choice, SurveyResult, Answer
from .models import Voting, VotingOption, Vote

class PollingListView(ListView):
    model = Survey
    template_name = "surveys/survey_list.html"

class SurveyDetailView(LoginRequiredMixin, DetailView):
    model = Survey
    template_name = "surveys/survey_detail.html"

class SurveyCreateView(LoginRequiredMixin, CreateView):
    model = Survey
    template_name = "surveys/survey_create.html"

class SurveyUpdateView(LoginRequiredMixin, UpdateView):
    model = Survey
    template_name = "surveys/survey_update.html"

class SurveyDeleteView(LoginRequiredMixin, DeleteView):
    model = Survey
    template_name = "surveys/survey_delete.html"

###

class VotingDetailView(LoginRequiredMixin, DetailView):
    model = Voting
    template_name = "voting/voting_detail.html"

class VotingCreateView(LoginRequiredMixin, CreateView):
    model = Voting
    template_name = "voting/voting_create.html"

class VotingUpdateView(LoginRequiredMixin, UpdateView):
    model = Voting
    template_name = "voting/voting_update.html"

class VotingDeleteView(LoginRequiredMixin, DeleteView):
    model = Voting
    template_name = "voting/voting_delete.html"
