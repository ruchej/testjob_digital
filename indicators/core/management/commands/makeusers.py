from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


User = get_user_model()


class Command(BaseCommand):
    help = '''
Создаёт тестовых пользователей login/password:
admin / admin,
user_1 / user_1,
user_2 / user_2
'''

    @staticmethod
    def create_super_user():
        '''Создаём супер пользователя'''

        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.loc',
                password='admin',
            )

    @staticmethod
    def create_test_users():
        '''Создадим двух тестовых пользоватлей'''

        for name in ('user_1', 'user_2'):
            if not User.objects.filter(username=name).exists():
                User.objects.create_user(
                    username=name,
                    email=f'{name}@example.loc',
                    password=name,
                    is_active=True
                )

    def handle(self, *args, **options):

        self.create_super_user()
        self.create_test_users()
