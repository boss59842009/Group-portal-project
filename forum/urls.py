from django.urls import path
from .views import ThreadCreateView, ThreadDeleteView, ThreadDetailView, ThreadListView, ThreadUpdateView

urlpatterns = [
    path('forum/', ThreadListView.as_view(), name='thread-list'),
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name='thread-detail'),
    path('thread/create/', ThreadCreateView.as_view(), name='thread-create'),
    path('thread/delete/<int:pk>/', ThreadDeleteView.as_view(), name='thread-delete'),
    path('thread/update/<int:pk>/', ThreadUpdateView.as_view(), name='thread-update'),
]