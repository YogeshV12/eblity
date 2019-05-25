from django.db import models

# Create your models here.

class Buttons(models.Model):
    stitched_start = models.BooleanField(default=True)
    stitched_stop = models.BooleanField(default=True)
    time_series_start = models.BooleanField(default=True)
    time_series_stop = models.BooleanField(default=True)