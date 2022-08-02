from django.contrib import admin
from core.models import Indicators


@admin.register(Indicators)
class IndicatorsAdmin(admin.ModelAdmin):
    pass
