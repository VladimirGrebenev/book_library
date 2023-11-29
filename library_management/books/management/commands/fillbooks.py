from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        # добавляем книги
        Book.objects.filter(title__startswith='test').delete()
        for i in range(10):
            Book.objects.create(
                title=f'testBook{i}',
                author=f'testAuthor{i}@mail.ru',
                publication_year=f'198{i}',
                isbn=f'978-985-13-9056-{i}'
            )