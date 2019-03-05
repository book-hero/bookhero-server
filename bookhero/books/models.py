from django.db import models
from attributes.models import Attribute


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    attributes = models.ManyToManyField(Attribute, through='BookAttributes')

    def __str__(self):
        return self.title


class BookAttributes(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.IntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
