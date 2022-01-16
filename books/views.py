from django.contrib import messages
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookForm
from .models import Book


def book_list(request):
    books = Book.active.all()
    return render(request, 'books/book_list.html', {'books':books})


def add_book(request):
    form = BookForm()
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Book successfully added')
            
            return redirect('book_list')
    
    context = {'form':form}
    
    return render(request, 'books/add_edit.html', context)


def edit_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    
    form = BookForm(instance=book)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Book successfully updated')
            
            return redirect('book_list')
    
    context = {'form':form}
    
    return render(request, 'books/add_edit.html', context)

def delete_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    
    if request.method == 'POST':
        book.is_active=False
        book.save()
        
        messages.warning(request, 'Book successfully deleted')
        
        return redirect('book_list')
    
    context = {'book':book}
    
    return render(request, 'books/delete_book.html', context)
