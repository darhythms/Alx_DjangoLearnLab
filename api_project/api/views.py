# api/views.py
from rest_framework.generics import ListAPIView  # Ensure this import is present
from .models import Book
from .serializers import BookSerializer

# Define the BookList view
class BookList(ListAPIView):
    queryset = Book.objects.all()  # Ensures all book objects are retrieved
    serializer_class = BookSerializer  # Defines the serializer used to format the data
