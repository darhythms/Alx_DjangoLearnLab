from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# @permission_required('your_app_name.can_view', raise_exception=True)
#def document_list(request):
#    documents = Document.objects.all()
 #   return render(request, 'your_template.html', {'documents': documents})

@permission_required('your_app_name.can_edit', raise_exception=True)
def edit_document(request, document_id):
    document = Document.objects.get(id=document_id)
    if request.method == 'POST':
        # Handle the edit logic here
        pass
    return render(request, 'edit_template.html', {'document': document})

#######################
from django.shortcuts import render, redirect
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # (e.g., save to database or send email)
            return redirect('success')  # Redirect to a success page
    else:
        form = ExampleForm()
    
    return render(request, 'example_template.html', {'form': form})

