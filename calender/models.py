from django.db import models

# Create your models here.

class Memo(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField()
  
class Diary(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()