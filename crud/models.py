from django.db import models

# Create your models here.
class student(models.Model):
    sid=models.CharField(max_length=100)
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()
    sadd=models.CharField(max_length=100)