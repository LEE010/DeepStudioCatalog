from django.db import models

# Create your models here.
class Tacotron(models.Model):
    type = models.CharField(max_length=200)
    target = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
