from django.urls import path
from advertisements import views
from advertisements.views import AdvertisementDeleteView, AdvertisementDetailView, AdvertisementUpdateView, AdvertisementListView, AdvertisementCreateView

app_name = 'advertisements'

urlpatterns = [
    path('', AdvertisementListView.as_view(), name='list'),
    path('<int:pk>/', AdvertisementDetailView.as_view(), name='detail'),
    path('create/', AdvertisementCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', AdvertisementUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', AdvertisementDeleteView.as_view(), name='delete'),
]