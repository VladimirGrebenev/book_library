from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import BookModelSerializer
from rest_framework.pagination import LimitOffsetPagination
from .models import Book
from .filters import BookFilter


class BookLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    pagination_class = BookLimitOffsetPagination
    filterset_class = BookFilter


