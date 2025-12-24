from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from events_calendar import models, forms

class EventsListView(ListView):
    model = models.Event
    context_object_name = 'events'
    template_name = 'events_calendar/events_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter_form'] = forms.EventsFilterForm(self.request.GET)
    #     return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
        


class EventsDetailView(DetailView):
    model = models.Event
    context_object_name = 'event-detail'
    template_name = 'events_calendar/events_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.EventForm(instance=self.object)
        return context
    
    def post(self, request, *args, **kwargs):
        event = forms.EventForm(instance=self.object)
        if event.is_valid():
            event.save()
            return redirect("event-detail", pk=event.task.pk)
        else:
            pass

class EventsCreateView(CreateView):
    model = models.Event
    form_class = forms.EventForm
    template_name = 'events_calendar/events_create.html'
    success_url = reverse_lazy("events-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventsUpdateView(UpdateView):
    model = models.Event
    form_class = forms.EventForm
    template_name = 'events_calendar/events_update.html'
    success_url = reverse_lazy("events-list")

class EventsDeleteView(DeleteView):
    model = models.Event
    template_name = 'events_calendar/events_delete.html'
    success_url = reverse_lazy("events-list")