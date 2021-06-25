from django.db import models

# Create your models here.
class Memo(models.Model):
    title = models.CharField(max_lengh=100)
    body = models.TextField()