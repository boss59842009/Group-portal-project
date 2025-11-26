from django.urls import path
from events_calendar.views import EventsListView, EventsDetailView, EventsCreatelView, EventsUpdateView, EventsDeleteView

urlpatterns = [
    path('events/', EventsListView.as_view(), name='events-list'),
    path('events/<int:pk>/', EventsDetailView.as_view(), name='event-detail'),
    path('events/create/', EventsCreatelView.as_view(), name='events-create'),
    path('events/update/<int:pk>/', EventsUpdateView.as_view(), name='events-update'),
    path('events/delete/<int:pk>/', EventsDeleteView.as_view(), name='events-delete'),
]