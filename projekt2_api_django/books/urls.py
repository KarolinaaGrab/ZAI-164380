from django.urls import path
from .views import *

urlpatterns = [
    path("books/", BookListCreateView.as_view(), name="book-list"),
    path("books/delete/", DeleteAllBooksView.as_view(), name="book-delete"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("import-books/", ImportBooksView.as_view(), name="import-books"),
]