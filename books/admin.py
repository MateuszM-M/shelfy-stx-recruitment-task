from django.contrib import admin
from .models import Book, Author


class AuthorInline(admin.StackedInline):
    model = Author
    extra = 1
    
    
class BookAdmin(admin.ModelAdmin):
    inlines = [AuthorInline]
    list_display = ['title','get_authors', 'published_date', 'isbn', 
                    'page_count', 'language']

    def get_authors(self, obj):
        authors = []
        for author in obj.authors.all():
            authors.append(author)
        return authors
    get_authors.short_description = 'Author'

admin.site.register(Book, BookAdmin)
