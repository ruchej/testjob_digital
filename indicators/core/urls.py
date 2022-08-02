from rest_framework.routers import SimpleRouter
from django.urls import path, include

from . import api


router = SimpleRouter()
router.register('indicators', api.IndicatorView)

urlpatterns = [
    path('', include(router.urls)),
]
