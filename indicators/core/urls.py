from rest_framework.routers import SimpleRouter
from django.urls import path, include

from . import api, views


router = SimpleRouter()
router.register('indicators', api.IndicatorView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.IndexView.as_view(), name='index'),
]
