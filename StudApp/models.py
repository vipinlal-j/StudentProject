from django.db import models

# Create your models here.
class StudentDB(models.Model):
    StudID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Age = models.CharField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Course = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
