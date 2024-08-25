from django.http import HttpResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    book_info = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(book_info, content_type="text/plain")
