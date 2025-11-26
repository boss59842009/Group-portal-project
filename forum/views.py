from django.shortcuts import render
from forum import models
from .models import Thread, Messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class ThreadListView(ListView):
    model = models.Thread
    context_object_name = "threads"
    template_name = "forum/thread_list.html"
    ordering = ['-created_at']

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        


class ThreadCreateView(CreateView):
    model = models.Thread
    template_name = "forum/thread_create.html"

class ThreadDetailView(DetailView):
    model = models.Thread
    context_object_name = "threads"
    template_name = "forum/thread_detail.html"

class ThreadUpdateView(UpdateView):
    model = models.Thread
    template_name = "forum/thread_update.html"

class ThreadDeleteView(DeleteView):
    model = models.Thread
    template_name = "forum/thread_delete.html"


#class MessagesCreateView(CreateView):
    #pass

#class MessagesUpdateView(UpdateView):
    #pass

#class MessagesDeleteView(DeleteView):
    #pass
