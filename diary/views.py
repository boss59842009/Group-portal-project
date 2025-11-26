from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class GradesListView(ListView):
    pass

class GradeCreateView(CreateView):
    pass

class GradeUpdateView(UpdateView):
    pass

class GradeDeleteView(DeleteView): 
    pass
