# api/views.py
from rest_framework.generics import ListAPIView  # Ensure this import is correct
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
