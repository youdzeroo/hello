from rest_framework import serializers
from core.models import Cars


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'

