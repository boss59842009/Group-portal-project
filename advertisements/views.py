from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Advertisement
from .forms import AdvertisementForm
from .mixins import AdvertisementManagePermissionMixin

class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisements_list.html'
    context_object_name = 'advertisements'

    def get_queryset(self):
        Advertisement.objects.filter(
            expiration_date__lt=timezone.now().date()
        ).delete()
        return Advertisement.objects.filter(is_active=True)

class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'advertisement/advertisement_detail.html'
    context_object_name = 'advertisement'

class AdvertisementCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'advertisement/advertisement_create.html'
    success_url = reverse_lazy('advertisements:list')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AdvertisementUpdateView(LoginRequiredMixin, AdvertisementManagePermissionMixin, UpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'advertisement/advertisement_update.html'
    success_url = reverse_lazy('advertisements:list')

class AdvertisementDeleteView(LoginRequiredMixin, AdvertisementManagePermissionMixin, DeleteView):
    model = Advertisement
    template_name = 'advertisement/advertisement_delete.html'
    success_url = reverse_lazy('advertisements:list')
