from django.http import HttpResponse
from .models import Book

#def book_list(request):
#    books = Book.objects.all()
#    book_info = "\n".join([f"{book.title} by {book.author.name}" for book in books])
#    return HttpResponse(book_info, content_type="text/plain")

def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/book_list.html', context)

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

