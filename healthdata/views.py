from django.shortcuts import render

from globalapp.views import BaseViews
from healthdata.models import HealthData
from healthdata.serializers import HealthDataSerializer

# Create your views here.
class HealthDataViewSet(BaseViews):
    model_name = HealthData
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]
    queryset = HealthData.objects.all()
    serializer_class = HealthDataSerializer