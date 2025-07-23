from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from Track.forms import TaskForm
from Track.models import Task
# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = "Track/task_list.html"

class TaskDetailView(DetailView):
    model = Task
    template_name="Track/task_detail.html"

class TaskCreateView(CreateView):
    model = Task
    template_name = 'Track/task_form.html'
    success_url = reverse_lazy('task_list')
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)