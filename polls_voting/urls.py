from django.urls import path
from . import views

urlpatterns = [
    path("polling/", views.PollingListView.as_view(), name="polling-list"),
    path("<int:pk>/", views.SurveyDetailView.as_view(), name="polling-detail"),
    path("<int:pk>/", views.SurveyCreateView.as_view(), name="polling-create"),
    path("<int:pk>/", views.SurveyUpdateView.as_view(), name="polling-update"),
    path("<int:pk>/", views.SurveyDeleteView.as_view(), name="polling-delete"),

    ###

    path("<int:pk>/", views.VotingDetailView.as_view(), name="voting-detail"),
    path("<int:pk>/", views.VotingDetailView.as_view(), name="voting-create"),
    path("<int:pk>/", views.VotingDetailView.as_view(), name="voting-update"),
    path("<int:pk>/", views.VotingDetailView.as_view(), name="voting-delete"),

]