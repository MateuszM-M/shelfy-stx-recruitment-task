from django.forms import ModelForm

from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'published_date', 'isbn', 
                    'page_count', 'language', 'image_link']
