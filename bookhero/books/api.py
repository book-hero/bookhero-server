from books.models import Book
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import BookSerializer
import requests


def formatOlDoc(doc):
    return {
        'id': 'OL',
        'authors': map(lambda author: {'name': author}, doc['author_name']),
        'open_library_cover_id': doc.get('cover_i'),
        'title': doc['title'],
        'subtitle': doc.get('subtitle')
    }


def serializeBook(book):
    serializer = BookSerializer(book)
    return serializer.data


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        title = self.request.query_params['title']
        title_args = title.split()
        title_args.append(title)
        base_qs = Book.objects.all()
        for word in title_args:
            base_qs = base_qs.filter(title__icontains=word)
        return base_qs

    @action(detail=False)
    def search(self, request):
        # Get search results from our database
        search_results = []
        books = self.get_queryset()
        search_results += map(serializeBook, books)
        try:
            response = requests.get(
                'http://openlibrary.org/search.json?title=' + request.query_params['title'])
            results = response.json()
            ol_results = map(formatOlDoc, results['docs'][:5])
            search_results += ol_results
        except Exception:
            print("open library isn't working")
        return Response(search_results)
