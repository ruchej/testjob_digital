from rest_framework.serializers import ModelSerializer
from core.models import Indicators


class IndicatorsSerializer(ModelSerializer):

    class Meta:
        model = Indicators
        fields = '__all__'
