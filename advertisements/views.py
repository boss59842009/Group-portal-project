from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def adv_list(request):
    return render(request, template_name="advertisement/edv_list.html")

class AdvertisementListView(ListView):
    pass
class AdvertisementDetailView(DetailView):
    pass

class AdvertisementCreateView(CreateView):
    pass

class AdvertisementUpdateView(UpdateView):
    pass

class AdvertisementDeleteView(DeleteView):
    pass
