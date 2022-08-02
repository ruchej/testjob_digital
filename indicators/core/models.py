from django.db import models
from django.conf import settings

from django.db.models.query import QuerySet


class Indicator(models.Model):

    class Meta:
        verbose_name = "Показатель"
        verbose_name_plural = "Показатели"

    fe = models.FloatField(default=0, verbose_name='Железо')
    si = models.FloatField(default=0, verbose_name='Кремний')
    al = models.FloatField(default=0, verbose_name='Алюминий')
    ca = models.FloatField(default=0, verbose_name='Кальций')
    s = models.FloatField(default=0, verbose_name='Сера')
    date = models.DateField(auto_now_add=True, verbose_name='Дата добавления данных')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Сотрудник')

    def __str__(self):
        return f'{self.user.username} от {self.date}'

    def get_by_year_month(self, year: int, month: int) -> QuerySet:
        '''Вернуть значения по данному году и месяцу'''
        queryset = self.objects.filter(date__year=year, date__month=month)
        return queryset
