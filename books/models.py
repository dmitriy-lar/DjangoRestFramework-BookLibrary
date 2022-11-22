from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=300)
    genre = models.ManyToManyField("Genres")
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    created = models.CharField(max_length=20)
    pages = models.IntegerField()
    synopsis = models.TextField()
    additional_information = models.TextField()


    def __str__(self):
        return self.title

class Genres(models.Model):
    title = models.CharField(max_length=300)


    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=300)
    date_of_birth = models.DateField()
    country_of_birth = models.CharField(max_length=100)
    additional_information = models.TextField()


    def __str__(self):
        return self.name