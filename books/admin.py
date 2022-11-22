from django.contrib import admin

from .models import Book, Genres, Author

admin.site.register(Book)
admin.site.register(Genres)
admin.site.register(Author)
