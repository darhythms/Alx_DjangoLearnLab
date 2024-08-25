from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Document

@permission_required('your_app_name.can_view', raise_exception=True)
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'your_template.html', {'documents': documents})

@permission_required('your_app_name.can_edit', raise_exception=True)
def edit_document(request, document_id):
    document = Document.objects.get(id=document_id)
    if request.method == 'POST':
        # Handle the edit logic here
        pass
    return render(request, 'edit_template.html', {'document': document})
