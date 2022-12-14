from rest_framework import serializers

from .models import Book, Genres, Author



""" Book Serializers """
class BookSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name="books-detail", lookup_field="pk"
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name="books-delete", lookup_field="pk"
    )
    edit_url = serializers.HyperlinkedIdentityField(
        view_name="books-edit", lookup_field="pk"
    )

    class Meta:
        model = Book
        fields = [
            "title",
            "genre",
            "author",
            "created",
            "pages",
            "synopsis",
            "additional_information",
            "detail_url",
            "delete_url",
            "edit_url",
        ]


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "title",
            "genre",
            "author",
            "created",
            "pages",
            "synopsis",
            "additional_information",
        ]


""" Author Serializers """
class AuthorListSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name="author-detail", lookup_field="pk"
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name="author-delete", lookup_field="pk"
    )
    edit_url = serializers.HyperlinkedIdentityField(
        view_name="author-edit", lookup_field="pk"
    )
    class Meta:
        model = Author
        fields = [
            'name',
            'date_of_birth',
            'country_of_birth',
            'additional_information',
            'detail_url',
            'edit_url',
            'delete_url',
        ]


class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'name',
            'date_of_birth',
            'country_of_birth',
            'additional_information',
        ]


""" Genre Serializers """
class GenreListSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name="genre-detail", lookup_field="pk"
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name="genre-delete", lookup_field="pk"
    )
    edit_url = serializers.HyperlinkedIdentityField(
        view_name="genre-edit", lookup_field="pk"
    )
    class Meta:
        model = Genres
        fields = [
            'title',
            'detail_url',
            'edit_url',
            'delete_url',
        ]


class GenreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = [
            'title',
        ]