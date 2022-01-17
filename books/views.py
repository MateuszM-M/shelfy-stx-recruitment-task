from django.contrib import messages
from django.core.paginator import Paginator
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render

from .filters import BookFilter
from .forms import BookForm
from .models import Book


def book_list(request):
    books = Book.active.all()
    
    book_filter = BookFilter(request.GET, queryset=books)
    books = book_filter.qs
    
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'book_filter': book_filter,
               'page_obj': page_obj}
    
    return render(request, 'books/book_list.html', context)


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
