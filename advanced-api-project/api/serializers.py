from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        if value > timezone.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


from rest_framework import serializers
from .models import Author
from .serializers import BookSerializer

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

# api/serializers.py
class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Includes custom validation to prevent future publication dates.
    """
    # Custom validation for publication_year

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Serializes the author name and all related books using the nested BookSerializer.
    """
    books = BookSerializer(many=True, read_only=True)
