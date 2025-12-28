from django.urls import path
from . import views

urlpatterns = [
    path("polling/", views.SurveyListView.as_view(), name="polling-list"),
    path("polling/<int:pk>/", views.SurveyDetailView.as_view(), name="polling-detail"),
    path("polling/create/", views.SurveyCreateView.as_view(), name="polling-create"),
    path("polling/update/<int:pk>/", views.SurveyUpdateView.as_view(), name="polling-update"),
    path("polling/delete/<int:pk>/", views.SurveyDeleteView.as_view(), name="polling-delete"),

    ###

    path("<int:pk>/", views.VotingDetailView.as_view(), name="voting-detail"),
    path("<int:pk>/", views.VotingDetailView.as_view(), name="voting-create"),
    path("<int:pk>/", views.VotingDetailView.as_view(), name="voting-update"),
    path("<int:pk>/", views.VotingDetailView.as_view(), name="voting-delete"),

]