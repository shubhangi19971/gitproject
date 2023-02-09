from django.db import models

class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=90)
    marks = models.FloatField()
    city = models.CharField(max_length=100)
