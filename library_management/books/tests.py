from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate
from .views import BookModelViewSet
from .models import Book
from users.models import CustomUser


# Create your tests here.

class TestBookModelViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/books/')
        view = BookModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        factory = APIRequestFactory()

        request = factory.post('/api/books/',
                               {'title': 'Название книги',
                                'author': 'Имя автора',
                                'publication_year': 2023,
                                'isbn': 12345678910},
                               format='json')
        view = BookModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/books/',
                               {'title': 'Название книги',
                                'author': 'Имя автора',
                                'publication_year': 2023,
                                'isbn': 12345678910},
                               format='json')
        admin = CustomUser.objects.create_superuser('admin@admin.com',
        'admin123456')
        force_authenticate(request, admin)
        view = BookModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)