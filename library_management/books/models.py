from django.db import models
from uuid import uuid4


class Book(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, verbose_name='id')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    isbn = models.TextField(max_length=250)

    class Meta:
        verbose_name = ("Книга")
        verbose_name_plural = ("Книги")

    def __str__(self):
        return self.title