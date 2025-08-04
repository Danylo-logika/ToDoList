from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

from Track.forms import TaskForm
from Track.models import Task
# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = "Track/task_list.html"

#class TaskDetailView(DetailView):
    #model = Task
    #template_name="Track/task_detail.html"

class TaskCreateView(CreateView):
    model = Task
    template_name = 'Track/task_form.html'
    success_url = reverse_lazy('task_list')
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'Track/task_delete.html'
    success_url = reverse_lazy('task_list')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'Track/task_detail.html'
    success_url = reverse_lazy('task_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.created_by != request.user:
            return HttpResponseForbidden("Ви не можете редагувати це завдання")
        return super().dispatch(request, *args, **kwargs)