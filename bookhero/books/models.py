from django.db import models
from bookhero.models import TimeStamped
from attributes.models import Attribute


# class Subject(TimeStamped):
#     name = models.CharField(max_length=100)


# class IdentifierType(TimeStamped):
#     name = models.CharField(max_length=100)


class Author(TimeStamped):
    name = models.CharField(max_length=100)
    # books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Book(TimeStamped):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    attributes = models.ManyToManyField(Attribute, through='BookAttribute')
    # synopsis = models.TextField(null=True)
    # publish_date = models.DateField(null=True)
    # subjects = models.ManyToManyField(Subject)
    open_library_cover_id = models.CharField(max_length=100, null=True)
    # open_library_url = models.CharField(max_length=255)

    def __str__(self):
        return self.title


# class Identifier(TimeStamped):
#     book = models.ForeignKey(Book, models.CASCADE)
#     identifier_type = models.ForeignKey(IdentifierType, models.CASCADE)
#     value = models.CharField(max_length=100)


class BookAttribute(TimeStamped):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.IntegerField
