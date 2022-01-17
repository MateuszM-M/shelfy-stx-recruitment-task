from rest_framework import viewsets, mixins

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    This viewset automatically provides `list` action.
    """
    queryset = Book.active.all()
    serializer_class = BookSerializer
