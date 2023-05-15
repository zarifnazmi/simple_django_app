from django.db import models

# Create your models here.

class Score(models.Model):
    user_id = models.IntegerField()
    value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)