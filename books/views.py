from django.forms import inlineformset_factory
from django.shortcuts import redirect, render

from .forms import BookForm
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books':books})


def add_book(request):
    form = BookForm()
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    
    context = {'form':form}
    
    return render(request, 'books/add_edit.html', context)
