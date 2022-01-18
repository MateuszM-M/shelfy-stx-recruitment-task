from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'published_date', 'isbn', 
                    'page_count', 'language', 'image_link']


class SearchApiForm(forms.Form):
    q = forms.CharField(label='q', max_length=100, required=False)
    title = forms.CharField(label='title', max_length=100, required=False)
    author = forms.CharField(label='author', max_length=100, required=False)
    isbn = forms.CharField(label='isbn', max_length=13, required=False)