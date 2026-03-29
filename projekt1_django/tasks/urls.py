from django.urls import path
from .views import *

# path("",...) - adres pusty wew aplikacji, tj. główna ścieżka tej aplikacji
# TaskListView.as_view() - klasa widoku zostaje zmieniona na widok Django metodą .as_view()
urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("task/add/", TaskCreateView.as_view(), name="task_add"),
    path("task/<int:pk>/edit/", TaskUpdateView.as_view(), name="task_edit"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),

    path("projects/", ProjectListView.as_view(), name="project_list"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    path("project/add/", ProjectCreateView.as_view(), name="project_add"),
    path("project/<int:pk>/edit/", ProjectUpdateView.as_view(), name="project_edit"),
    path("project/<int:pk>/delete/", ProjectDeleteView.as_view(), name="project_delete"),

    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tag/add/", TagCreateView.as_view(), name="tag_add"),
    path("tag/<int:pk>/edit/", TagUpdateView.as_view(), name="tag_edit"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
]
