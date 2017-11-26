from django.db import models

# Create your models here.
class Score(models.Model):
    playerName = models.CharField(max_length=50)
    acumScore = models.IntegerField(default=0)
