from django.db import models

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

