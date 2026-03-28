from django.contrib import admin
from .models import Task, Project, Tag

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at") # kolumny w tabeli
    search_fields = ("name",) # wyszukiwarka

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "status", "due_date", "created_at")
    list_filter = ("status", "project", "tags") # filtry po prawej
    search_fields = ("title", "description")
