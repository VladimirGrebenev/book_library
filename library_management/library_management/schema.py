import graphene
from graphene_django import DjangoObjectType
from users.models import CustomUser
from books.models import Book


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(CustomUserType)
    all_books = graphene.List(BookType)
    user_by_user_name = graphene.Field(CustomUserType, user_name=graphene.String(required=True))
    books_by_author = graphene.List(BookType, author=graphene.String(
        required=False))

    def resolve_all_users(root, info):
        return CustomUser.objects.all()

    def resolve_user_by_user_name(self, info, user_name):
        try:
            return CustomUser.objects.get(user_name=user_name)
        except CustomUser.DoesNotExist:
            return None

    def resolve_all_books(root, info):
        return Book.objects.all()

    def resolve_books_by_author(self, info, author=None):
        books = Book.objects.all()
        if author:
            books = books.filter(books__author=author)
        return books

schema = graphene.Schema(query=Query)