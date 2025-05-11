from django.db import models

# Create your models here.
class MeritListEntry(models.Model):
    applicant_name = models.CharField(max_length=100)
    batch = models.CharField(max_length=10)
    roll = models.CharField(max_length=20, unique=True)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    rank = models.PositiveIntegerField()
    sl = models.PositiveIntegerField(verbose_name="Serial")
    subject = models.CharField(max_length=100)
    level = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.applicant_name} - {self.subject} ({self.roll})"