from django.urls import path

from .views import (
    BookListAPIView,
    BookDetailAPIVIew
)

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='books-list'),
    path('books/<int:pk>', BookDetailAPIVIew.as_view(), name='books-detail'),
]