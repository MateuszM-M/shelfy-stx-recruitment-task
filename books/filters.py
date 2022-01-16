import django_filters
from django_filters import DateFilter, CharFilter

from .models import Book


class BookFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    authors = CharFilter(field_name='authors', lookup_expr='icontains')
    language = CharFilter(field_name='language', lookup_expr='icontains')
    start_date = DateFilter(field_name="published_date", lookup_expr='gte')
    end_date = DateFilter(field_name="published_date", lookup_expr='lte')
    
    class Meta:
        mordel = Book
