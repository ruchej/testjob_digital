from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from .models import Indicator
from .filters import IndicatorFilter
from .serializers import IndicatorSerializer


class ReadOnly(BasePermission):

    def has_permissions(self, request, view):
        return request.method in SAFE_METHODS


class SafeModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ReadOnly]


class IndicatorView(SafeModelViewSet):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer
    filer_backends = (filters.DjangoFilterBackend,)
    filterset_class = IndicatorFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
