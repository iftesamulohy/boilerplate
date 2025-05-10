from django.db import models

from globalapp.models import Common
from users.models import Users

# Create your models here.
class HealthData(Common):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    activity_level = models.CharField(max_length=50)
    sleep_hours = models.FloatField(null=True, blank=True)
    source = models.CharField(max_length=50)  # e.g., Google Fit, Apple HealthKit, Manual