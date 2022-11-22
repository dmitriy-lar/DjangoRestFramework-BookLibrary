from rest_framework.generics import ListAPIView

from .models import Book

class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()


