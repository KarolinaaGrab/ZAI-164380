from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255, blank=True)
    first_publish_year = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=100, default="Open Library")

    def __str__(self):
        return self.title