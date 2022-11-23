from django.urls import path

from .views import (
    BookListAPIView,
    BookDetailAPIVIew,
    BookUpdateAPIVIew,
    BookDeleteAPIVIew,
    BookCreateAPIView,
    AuthorListAPIView
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

]