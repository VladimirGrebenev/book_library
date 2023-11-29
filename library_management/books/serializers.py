from rest_framework import serializers
from .models import Book

class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year', 'isbn']


class BookModelSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']