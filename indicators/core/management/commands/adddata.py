import datetime
import random

from django.db import transaction
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from core.models import Indicator


User = get_user_model()


class Command(BaseCommand):
    help = 'Создаёт тестовые данные'

    def handle(self, *args, **options):

        users = []
        for u in User.objects.all():
            if u.username != 'admin':
                users.append(u)

        if not users:
            raise ValueError('Пользователей в системе нет')

        start_date = datetime.date(2022, 1, 1)
        end_date = datetime.date(2022, 12, 30)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days

        with transaction.atomic():
            for i in range(100):
                user = random.choice(users)
                random_number_of_days = random.randrange(days_between_dates)
                random_date = start_date + datetime.timedelta(days=random_number_of_days)

                Indicator.objects.create(
                    fe=round(random.uniform(0, 20.0), 2),
                    si=round(random.uniform(0, 20.0), 2),
                    al=round(random.uniform(0, 20.0), 2),
                    ca=round(random.uniform(0, 20.0), 2),
                    s=round(random.uniform(0, 20.0), 2),
                    user=user,
                    date=random_date
                )

