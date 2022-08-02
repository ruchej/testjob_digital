from django_filters import rest_framework as filters

from core.models import Indicator


class IndicatorFilter(filters.FilterSet):
    year = filters.NumberFilter(field_name='date', lookup_expr='year')
    month = filters.NumberFilter(field_name='date', lookup_expr='month')

    class Meta:
        model = Indicator
        fields = ('date',)
