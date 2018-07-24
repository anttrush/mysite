from django.db import models

# Create your models here.
class Developer(models.Model):
    dev_id = models.IntegerField()
    dev_name = models.CharField(max_length=100)
    dev_score_Documentation = models.FloatField(default=0)
    dev_score_CodeStyle = models.FloatField(default=0)
    dev_score_Performance = models.FloatField(default=0)
    dev_score_BestPractices = models.FloatField(default=0)
    dev_score_Security = models.FloatField(default=0)
    dev_score_Multithreading = models.FloatField(default=0)
    dev_score_Design = models.FloatField(default=0)
    dev_score_ErrorProne = models.FloatField(default=0)
    dev_score_All = models.FloatField(default=0)

    def __str__(self):
        return self.dev_name


class Project(models.Model):
    proj_id = models.IntegerField()
    proj_name = models.CharField(max_length=100)
    proj_stars = models.IntegerField(default=0)
    def __str__(self):
        return self.proj_name
