from django.db import models

class task(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    Desc = models.CharField(max_length=30)
    Date = models.DateField(max_length=30)
