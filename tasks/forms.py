from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput
from .models import Task, Project


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "project", "due_date", "tags"]
        widgets = {
            "due_date": DateInput(
                attrs={"class": "form-control", "type": "date"},
                format="%d-%m-%Y"),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]

        if "test" in title.lower():
            raise ValidationError("Tytuł nie może zawierać słowa 'test'.")

        return title

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description"]
