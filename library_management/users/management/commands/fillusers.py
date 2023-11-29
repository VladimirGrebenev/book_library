from django.core.management.base import BaseCommand
from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        # добавляем тестовых пользователей
        CustomUser.objects.filter(email__startswith='test').delete()
        for i in range(3):
            CustomUser.objects.create_user(
                user_name=f'testName{i}',
                email=f'testMail{i}@mail.ru',
                password=f'test{i}'
            )

        # добавляем тестового админа superuser:
        # login/email: admin@mail.ru pass: admin
        CustomUser.objects.filter(email='admin@mail.ru').delete()
        CustomUser.objects.create_superuser('admin@mail.ru', 'admin',
                                            user_name='admin')
