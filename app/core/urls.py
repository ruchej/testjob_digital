from rest_framework.routers import SimpleRouter
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from . import api, views


schema_view = get_swagger_view(title='Pastebin API')

router = SimpleRouter()
router.register('indicators', api.IndicatorView)


urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.IndexView.as_view(), name='index'),
    path('docs/', schema_view),
]
