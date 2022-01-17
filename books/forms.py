from django.forms import ModelForm, Form

from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'published_date', 'isbn', 
                    'page_count', 'language', 'image_link']


class SearchApiForm(Form):
    search = forms.CharField(label='search', max_length=100)
    title = forms.CharField(label='title', max_length=100)
    author = forms.CharField(label='author', max_length=100)
    isbn = forms.CharField(label='author', max_length=13)