from django.shortcuts import render, redirect
from forum import models, forms
from .models import Thread, Messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from forum.mixins import UserIsOwnerMixin

class ThreadListView(ListView):
    model = models.Thread
    context_object_name = "threads"
    template_name = "forum/thread_list.html"
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = forms.ThreadsFilterForm(self.request.GET)
        return context

class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = models.Thread
    form_class = forms.ThreadForm
    template_name = 'forum/thread_create.html'
    success_url = reverse_lazy("thread-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ThreadDetailView(DetailView):
    model = models.Thread
    context_object_name = "thread"
    template_name = 'forum/thread_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message_form"] = forms.MessageForm()
        context["messages"] = self.object.messages.order_by("-created_at")
        print(context["messages"])
        return context
    
    def post(self, request, *args, **kwargs):
        message_form = forms.MessageForm(request.POST, request.FILES)
        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.user = request.user
            message.thread = self.get_object()
            message.save()
            return redirect("thread-detail", pk=message.thread.pk)
        else:
            context = self.get_context_data(form=forms)
            return context


class ThreadUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = models.Thread
    form_class = forms.ThreadForm
    template_name = 'forum/thread_update.html'
    success_url = reverse_lazy("thread-list")

class ThreadDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = models.Thread
    template_name = 'forum/thread_delete.html'
    success_url = reverse_lazy("thread-list")
