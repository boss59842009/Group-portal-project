from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from events_calendar import models, forms

class EventsListView(ListView):
    model = models.Event
    context_object_name = 'events'
    template_name = 'tasks/...html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter_form'] = forms.EventsFilterForm(self.request.GET)
    #     return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
        


class EventsDetailView(DetailView):
    pass

class EventsCreatelView(CreateView):
    pass

class EventsUpdateView(UpdateView):
    pass

class EventsDeleteView(DeleteView):
    pass