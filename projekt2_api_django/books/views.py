from django.shortcuts import render
import requests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book
from .filters import BookFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BookFilter
    search_fields = ["title", "author_name"]
    ordering_fields = ["id", "author_name", "first_publish_year", "title"]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == "DELETE":
            return [IsAuthenticated()]
        return [AllowAny()]

class DeleteAllBooksView(APIView):
    def delete(self, request):
        deleted_count, _ = Book.objects.all().delete()
        return Response(
            {"message": f"Usunięto {deleted_count} książek."},
            status=status.HTTP_200_OK
        )

class ImportBooksView(APIView):
    def post(self, request):
        url = f"https://openlibrary.org/search.json?q=python"
        response = requests.get(url)

        if response.status_code != 200:
            return Response(
                {"error": "Nie udało się pobrać danych z Open Library"},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = response.json()
        docs = data.get("docs", [])[:20]

        created_books = []

        for item in docs:
            title = item.get("title", "")
            author_names = item.get("author_name", [])
            author_name = author_names[0] if author_names else ""
            first_publish_year = item.get("first_publish_year")

            # get_or_create zwraca (obiekt, created)
            book, created = Book.objects.get_or_create(
                title=title,
                author_name=author_name,
                first_publish_year=first_publish_year,
                source="Open Library"
            )

            created_books.append(book)

        serializer = BookSerializer(created_books, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)