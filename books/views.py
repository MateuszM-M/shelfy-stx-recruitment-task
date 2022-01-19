from django.contrib import messages
from django.core.paginator import Paginator
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render

from .filters import BookFilter
from .forms import BookForm, SearchApiForm
from .models import Book

from.import_api import search_api, render_to_table


def book_list(request):
    """Main page view with main table with books from database,
    filters and pagination
    """
    
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
    """Add book view with functionality of rendering Google
    Books API to table and import to db
    """
    form = BookForm()
    search_api_form = SearchApiForm()
    import_books = {}
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Book successfully added')
            
            return redirect('book_list')
        
    if request.method == 'GET' and 'search_book' in request.GET:
        search_api_form = SearchApiForm(request.GET)
        if search_api_form.is_valid():
            queries = search_api_form.cleaned_data
            search = search_api(queries=queries)
            import_books = render_to_table(books=search)
            
            
    context = {'form':form, 'search_api_form':search_api_form,
               'import_books': import_books}
    
    return render(request, 'books/add_edit.html', context)


def import_book(request):
    """View to import to database from
    Google Book API results
    """
    if request.method == 'POST':
        book = Book.objects.create(
            title=request.POST.get('title'),
            authors=request.POST.get('authors'),
            published_date=request.POST.get('published_date'),
            isbn=request.POST.get('isbn'),
            page_count=request.POST.get('page_count'),
            image_link=request.POST.get('image_link'),
            language=request.POST.get('language')
        )
        return redirect('book_list')

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
    """ Soft delete view. Sets book is_active to false
    """
    book = get_object_or_404(Book, id=pk)
    
    if request.method == 'POST':
        book.is_active=False
        book.save()
        
        messages.warning(request, 'Book successfully deleted')
        
        return redirect('book_list')
    
    context = {'book':book}
    
    return render(request, 'books/delete_book.html', context)
