from django.contrib import admin
from core.models import Indicator


@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'fe', 'si', 'al', 'ca', 's', 'date')
    list_filter = ('date', 'user')
