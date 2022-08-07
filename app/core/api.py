from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from django_filters import rest_framework as filters
from django.db.models import Max, Min, Avg

from .models import Indicator
from .filters import IndicatorFilter
from .serializers import IndicatorSerializer, IndicatorListSerializer


class ReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IndicatorView(ListModelMixin, CreateModelMixin, GenericViewSet):

    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer
    filer_backends = (filters.DjangoFilterBackend,)
    filterset_class = IndicatorFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if getattr(self, 'action') == 'list':
            return IndicatorListSerializer
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        stats = queryset.aggregate(
            Max('fe'), Max('si'), Max('al'), Max('ca'), Max('s'),
            Min('fe'), Min('si'), Min('al'), Min('ca'), Min('s'),
            Avg('fe'), Avg('si'), Avg('al'), Avg('ca'), Avg('s'),
        )
        serializer = self.get_serializer({'data': queryset, 'stats':stats})
        return Response(serializer.data)

    #def create(self, request, *args, **kwargs):

    #    print(type(request.data))
    #    is_many = isinstance(request.data, list)
    #    if not is_many:
    #        return super().create(request, *args, **kwargs)
    #    else:
    #        serializer = self.get_serializer(data=request.data, many=True)
    #        serializer.is_valid(raise_exception=True)
    #        self.perform_create(serializer)
    #        headers = self.get_success_headers(serializer.data)
    #        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
