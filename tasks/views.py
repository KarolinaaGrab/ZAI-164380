from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task, Project
from .forms import TaskForm, ProjectForm


# Create your views here.
class TaskListView(ListView): # ListView - gotowy widok generyczny Django
    model = Task # z jakiego modelu pobrać dane
    template_name = "tasks/task_list.html" # który plik html użyć
    context_object_name = "tasks" # w szablonie używamy zmiennej "tasks" zamiast domyślnego task_list

class TaskDetailView(DetailView): # pobiera jeden obiekt na podstawie pk -> przekazuje go do template
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task" # w szablonie używamy task

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("task_list")


class ProjectListView(ListView):
    model = Project
    template_name = "tasks/project_list.html"
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    model = Project
    template_name = "tasks/project_detail.html"
    context_object_name = "project"


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "tasks/project_form.html"
    success_url = reverse_lazy("project_list")


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "tasks/project_form.html"
    success_url = reverse_lazy("project_list")


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "tasks/project_confirm_delete.html"
    success_url = reverse_lazy("project_list")

