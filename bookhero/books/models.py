from django.db import models
from attributes.models import Attribute


class Subject(models.Model):
    name = models.CharField(max_length=100)


class IdentifierType(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    attributes = models.ManyToManyField(Attribute, through='BookAttribute')
    synopsis = models.TextField(null=True)
    publish_date = models.DateField(null=True)
    subjects = models.ManyToManyField(Subject)
    open_library_cover_id = models.CharField(max_length=100, null=True)
    open_library_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Identifier(models.Model):
    book = models.ForeignKey(Book, models.CASCADE)
    identifier_type = models.ForeignKey(IdentifierType, models.CASCADE)
    value = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class BookAttribute(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.IntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
