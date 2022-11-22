from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)

from .models import Book

from .serializers import BookSerializer

class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailAPIVIew(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
