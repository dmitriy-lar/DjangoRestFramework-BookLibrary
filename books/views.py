from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

from .models import Book, Genres, Author

from .serializers import (
    BookSerializer,
    BookCreateSerializer,
    AuthorListSerializer,
)

from django.db.models import Q


""" Books API Views """

class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    pagination_class = PageNumberPagination



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


""" Genres API Views """

""" Authors API Views """
class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer