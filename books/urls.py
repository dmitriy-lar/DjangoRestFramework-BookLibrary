from django.urls import path

from .views import (
    # Books
    BookListAPIView,
    BookDetailAPIVIew,
    BookUpdateAPIVIew,
    BookDeleteAPIVIew,
    BookCreateAPIView,
    # Authors
    AuthorListAPIView,
    AuthorDetailAPIView,
    AuthorUpdateAPIVIew,
    AuthorDeleteAPIVIew,
    AuthorCreateAPIView,
    # Genres
    GenreListApiView,
    GenreDetailAPIView,
    GenreUpdateAPIVIew,
    GenreDeleteAPIVIew,

)

urlpatterns = [
    # Book urls
    path('books/', BookListAPIView.as_view(), name='books-list'),
    path('books/<int:pk>/', BookDetailAPIVIew.as_view(), name='books-detail'),
    path('books/<int:pk>/edit/', BookUpdateAPIVIew.as_view(), name='books-edit'),
    path('books/<int:pk>/delete/', BookDeleteAPIVIew.as_view(), name='books-delete'),
    path('books/create/', BookCreateAPIView.as_view(), name='books-create'),

    # Author urls
    path('authors/', AuthorListAPIView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(), name='author-detail'),
    path('authors/<int:pk>/edit/', AuthorUpdateAPIVIew.as_view(), name='author-edit'),
    path('authors/<int:pk>/delete/', AuthorDeleteAPIVIew.as_view(), name='author-delete'),
    path('authors/create/', AuthorCreateAPIView.as_view(), name='authors-create'),

    # Genre urls
    path('genres/', GenreListApiView.as_view(), name='genre-list'),
    path('genres/<int:pk>/', GenreDetailAPIView.as_view(), name='genre-detail'),
    path('genres/<int:pk>/edit/', GenreUpdateAPIVIew.as_view(), name='genre-edit'),
    path('genres/<int:pk>/delete/', GenreDeleteAPIVIew.as_view(), name='genre-delete'),

]