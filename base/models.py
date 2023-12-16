from django.db import models

# Create your models here.
class Grade(models.Model):
    unit = models.name = models.ForeignKey('Unit', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    

class Unit(models.Model):
    problem = models.name = models.ForeignKey('Problem', on_delete=models.CASCADE)
    unit_number = models.IntegerField()
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)

class Problem(models.Model):
    question = models.CharField(max_length=50, null=True)
    expression = models.CharField(max_length=20, null=False)
    answer = models.IntegerField(blank=False, null=False)