from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .models import Book

from .serializers import BookSerializer

class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailAPIVIew(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateAPIVIew(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteAPIVIew(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
