from django.db import models

# Create your models here.
class Developer(models.Model):
    dev_id = models.IntegerField()
    dev_name = models.CharField(max_length=100)

    dev_score_CodeStyle = models.FloatField(default=0)
    dev_score_Design = models.FloatField(default=0)
    dev_score_Documentation = models.FloatField(default=0)
    dev_score_ErrorProne = models.FloatField(default=0)
    dev_score_Performance = models.FloatField(default=0)
    dev_score_Multithreading = models.FloatField(default=0)
    dev_score_Security = models.FloatField(default=0)
    dev_score_Others = models.FloatField(default=0)

    # multith, net, database, IO, text, GUI, math, other
    dev_score_text = models.FloatField(default=0)
    dev_score_graph = models.FloatField(default=0)
    dev_score_math = models.FloatField(default=0)
    dev_score_net = models.FloatField(default=0)
    dev_score_IO = models.FloatField(default=0)
    dev_score_database = models.FloatField(default=0)
    dev_score_secure = models.FloatField(default=0)
    dev_score_other = models.FloatField(default=0)

    dev_score_Efficient = models.FloatField(default=0)

    dev_score_cLOC = models.IntegerField(default=0)
    dev_follower_Number = models.IntegerField(default=0)


    # dev_score_All = models.FloatField(default=0)
    # dev_project = models.CharField(max_length=100, default="None")

    def __str__(self):
        return self.dev_name


class Project(models.Model):
    proj_id = models.IntegerField()
    proj_name = models.CharField(max_length=100)
    proj_stars = models.IntegerField(default=0)
    proj_owner = models.IntegerField()

    def __str__(self):
        return self.proj_name
