from rest_framework.serializers import ModelSerializer
from core.models import Indicator


class IndicatorSerializer(ModelSerializer):

    class Meta:
        model = Indicator
        fields = '__all__'