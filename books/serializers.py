from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'title',
            'genre',
            'author',
            'created',
            'pages',
            'synopsis',
            'additional_information'
        ]


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'title',
            'genre',
            'author',
            'created',
            'pages',
            'synopsis',
            'additional_information'
        ]