from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.filters import SearchFilter

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    This viewset automatically provides `list` action.
    """
    queryset = Book.active.all()
    serializer_class = BookSerializer
    
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = {
        'title': ['icontains'], 
        'authors': ['icontains'], 
        'language': ['icontains'],
        'published_date': ['gte', 'lte']
        }
    search_fields = ['title', 'authors', 'language']
