from django.db import models
from django.utils import timezone

# Create your models here.

class Buttons(models.Model):
    stitched_start = models.BooleanField(default=True)
    stitched_stop = models.BooleanField(default=True)
    time_series_start = models.BooleanField(default=True)
    time_series_stop = models.BooleanField(default=True)



class Alerts(models.Model):
    StudentName = models.TextField()
    Grade = models.IntegerField()
    Date = models.TextField()
    Concept = models.TextField()
    ConceptProgress = models.IntegerField()
    SubConcept = models.TextField()
    SubConceptProgress = models.IntegerField()
    PerSolved = models.IntegerField()
    AverageTimePerQuestion = models.IntegerField()
    LGD = models.IntegerField()
    LGR = models.IntegerField()
    PerLearningGapResolved = models.TextField()
    comment = models.TextField()
    status = models.IntegerField(default=0)


class Comments(models.Model):
    cmt_id = models.IntegerField(unique = False)
    text = models.TextField()
    time_stamp = models.DateTimeField(timezone.now, auto_now=True)

class Interventions(models.Model):
    alert_id = models.IntegerField()
    interv_id = models.IntegerField()
    interv_type = models.IntegerField()
    asgn_to = models.IntegerField()
    follow_up_by = models.TextField()
    interv_status = models.IntegerField()
    rating = models.IntegerField()
