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
    AuthorCreateSerializer,
    GenreListSerializer,
)

from django.db.models import Q


""" Books API Views """

class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination



class BookDetailAPIVIew(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateAPIVIew(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]


class BookDeleteAPIVIew(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]


class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    permission_classes = [IsAdminUser]


""" Genres API Views """
class GenreListApiView(ListAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreListSerializer


class GenreDetailAPIView(RetrieveAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreListSerializer


class GenreUpdateAPIVIew(UpdateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreListSerializer
    # permission_classes = [IsAdminUser]


class GenreDeleteAPIVIew(DestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreListSerializer
    # permission_classes = [IsAdminUser]



""" Authors API Views """
class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination


class AuthorDetailAPIView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer
    permission_classes = [IsAuthenticated]


class AuthorUpdateAPIVIew(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer
    permission_classes = [IsAdminUser]


class AuthorDeleteAPIVIew(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer
    permission_classes = [IsAdminUser]


class AuthorCreateAPIView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorCreateSerializer
    permission_classes = [IsAdminUser]