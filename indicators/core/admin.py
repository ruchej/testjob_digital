from django.contrib import admin
from core.models import Indicator


@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    pass
