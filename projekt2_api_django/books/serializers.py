from rest_framework import serializers
from .models import Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate_title(self, value):
        value = value.strip()
        if len(value) < 2:
            raise serializers.ValidationError("Tytuł jest za krótki")
        return value

    def validate_author_name(self, value):
        if not value:
            raise serializers.ValidationError("Autor nie może być pusty")
        return value

    def validate_first_publish_year(self, value):
        if value:
            current_year = datetime.now().year
            if value > current_year:
                raise serializers.ValidationError("Rok nie może być z przyszłości")
        return value

    def validate(self, data):
        if Book.objects.filter(
                title=data.get('title'),
                author_name=data.get('author_name')
        ).exists():
            raise serializers.ValidationError("Ta książka już istnieje")
        return data
