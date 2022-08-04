from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.fields import DecimalField
from core.models import Indicator


class IndicatorSerializer(ModelSerializer):

    class Meta:
        model = Indicator
        fields = '__all__'
        read_only_fields = ['user']


class IndicatorStatsSerializer(Serializer):

    fe_max = DecimalField(max_digits=5, decimal_places=2, source='fe__max')
    si_max = DecimalField(max_digits=5, decimal_places=2, source='si__max')
    al_max = DecimalField(max_digits=5, decimal_places=2, source='al__max')
    ca_max = DecimalField(max_digits=5, decimal_places=2, source='ca__max')
    s_max = DecimalField(max_digits=5, decimal_places=2, source='s__max')

    fe_min = DecimalField(max_digits=5, decimal_places=2, source='fe__min')
    si_min = DecimalField(max_digits=5, decimal_places=2, source='si__min')
    al_min = DecimalField(max_digits=5, decimal_places=2, source='al__min')
    ca_min = DecimalField(max_digits=5, decimal_places=2, source='ca__min')
    s_min = DecimalField(max_digits=5, decimal_places=2, source='s__min')

    fe_avg = DecimalField(max_digits=5, decimal_places=2, source='fe__avg')
    si_avg = DecimalField(max_digits=5, decimal_places=2, source='si__avg')
    al_avg = DecimalField(max_digits=5, decimal_places=2, source='al__avg')
    ca_avg = DecimalField(max_digits=5, decimal_places=2, source='ca__avg')
    s_avg = DecimalField(max_digits=5, decimal_places=2, source='s__avg')



class IndicatorListSerializer(Serializer):
    data = IndicatorSerializer(many=True)
    stats = IndicatorStatsSerializer()
