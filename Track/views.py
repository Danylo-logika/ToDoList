from django.shortcuts import render
from django.views.generic import ListView, DetailView

from Track.models import Task
# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = "Track/task_list.html"

class TaskDetailView(DetailView):
    model = Task
    temlate_name="Track/task_detail.html"