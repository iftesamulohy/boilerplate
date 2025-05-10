from rest_framework import serializers

from healthdata.models import HealthData
class HealthDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthData
        fields = '__all__'