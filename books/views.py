from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView
)

from .models import Book

from .serializers import (
    BookSerializer,
    BookCreateSerializer,
)


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


class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
