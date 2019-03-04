from rest_framework import serializers
from books.models import Book

# Book Serializer


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
