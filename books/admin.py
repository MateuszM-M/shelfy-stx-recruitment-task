from django.contrib import admin
from .models import Book
   
    
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','authors', 'published_date', 'isbn', 
                    'page_count', 'language']


admin.site.register(Book, BookAdmin)
