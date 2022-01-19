import django_filters
from django_filters import CharFilter, DateFilter

from .models import Book


class BookFilter(django_filters.FilterSet):
    """ 
    Django filter used for filtering main table
    in book list view
    """
    
    title = CharFilter(field_name='title', lookup_expr='icontains',
                       label='Title: ')
    authors = CharFilter(field_name='authors', lookup_expr='icontains',
                         label='Author:')
    language = CharFilter(field_name='language', lookup_expr='icontains',
                          label='Language: ')
    start_date = DateFilter(field_name="published_date", lookup_expr='gte')
    end_date = DateFilter(field_name="published_date", lookup_expr='lte')
    
    class Meta:
        mordel = Book
