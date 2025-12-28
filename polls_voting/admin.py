from django.contrib import admin
from .models import Survey, Question, SurveyResult, Voting, VotingOption, Vote

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(SurveyResult)
admin.site.register(Voting)
admin.site.register(VotingOption)
admin.site.register(Vote)