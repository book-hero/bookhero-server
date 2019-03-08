from rest_framework import serializers
from rest_framework.parsers import JSONParser
import requests


class OLBook(object):
    def __init__(self, title, authors, subjects, publish_date, url):
        self.title = title
        self.authors = authors
        # self.identifiers = identifiers
        self.subjects = subjects
        self.publish_date = publish_date
        self.url = url

    def __str__(self):
        return self.title


class SubjectSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=100)


class AuthorSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=100)


class OLBookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    authors = AuthorSerializer(many=True)
    subjects = SubjectSerializer(many=True)
    publish_date = serializers.DateField(input_formats=["%B %Y", "%B %d, %Y"])
    url = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return OLBook(**validated_data)


def get_open_library_book_info(isbn):
    url = 'https://openlibrary.org/api/books'
    params = {'bibkeys': 'ISBN:' + isbn, 'format': 'json', 'jscmd': 'data'}
    response = requests.get(url, params=params)
    data = response.json()["ISBN:" + isbn]
    serializer = OLBookSerializer(data=data)
    serializer.is_valid()

    return serializer.save()
