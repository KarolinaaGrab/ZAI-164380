from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author_name", "first_publish_year", "source")
    list_filter = ("author_name", )
    search_fields = ("title", "author_name")