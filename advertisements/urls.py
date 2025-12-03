from django.urls import path
from advertisements import views
from advertisements.views import AdvertisementDeleteView, AdvertisementDetailView, AdvertisementUpdateView, adv_list

urlpatterns = [
    path('advertisements/', adv_list, name='advertisements-list'),
    path("advertisement/<int:pk>/", AdvertisementDetailView.as_view(), name='advertisement-detail'),
    path("advertisement/create/", AdvertisementDetailView.as_view(), name='advertisement-create'),
    path("advertisement/update/<int:pk>/", AdvertisementUpdateView.as_view(), name='advertisement-update'),
    path("advertisement/delete/<int:pk>/", AdvertisementDeleteView.as_view(), name='advertisement-delete'),
]