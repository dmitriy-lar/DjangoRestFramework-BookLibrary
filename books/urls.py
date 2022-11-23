from django.urls import path

from .views import (
    BookListAPIView,
    BookDetailAPIVIew,
    BookUpdateAPIVIew,
    BookDeleteAPIVIew,
    BookCreateAPIView,
    AuthorListAPIView,
    AuthorDetailAPIView,
    AuthorUpdateAPIVIew,
    AuthorDeleteAPIVIew,
    AuthorCreateAPIView,
)

urlpatterns = [
    # Book urls
    path('books/', BookListAPIView.as_view(), name='books-list'),
    path('books/<int:pk>/', BookDetailAPIVIew.as_view(), name='books-detail'),
    path('books/<int:pk>/edit', BookUpdateAPIVIew.as_view(), name='books-edit'),
    path('books/<int:pk>/delete', BookDeleteAPIVIew.as_view(), name='books-delete'),
    path('books/create/', BookCreateAPIView.as_view(), name='books-create'),

    # Author urls
    path('authors/', AuthorListAPIView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(), name='author-detail'),
    path('authors/<int:pk>/edit', AuthorUpdateAPIVIew.as_view(), name='author-edit'),
    path('authors/<int:pk>/delete', AuthorDeleteAPIVIew.as_view(), name='author-delete'),
    path('authors/create/', AuthorCreateAPIView.as_view(), name='authors-create'),

]