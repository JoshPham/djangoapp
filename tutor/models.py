from django.db import models

# Create your models here.
class Grade(models.Model):
    grade_id = models.IntegerField(default=3)
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    units = models.name = models.ManyToManyField("Unit", limit_choices_to={'grade_id__icontains': grade_id})
    
    def __str__(self):
        return f'{self.title}'

class Unit(models.Model):
    grade_id = models.IntegerField(default=3)
    unit_id = models.IntegerField()
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    problems = models.name = models.ManyToManyField("Problem", limit_choices_to={'unit_id__icontains': unit_id})
    
    def __str__(self):
        return f'Unit {self.unit_id} - {self.title} (Grade {self.grade_id})'

class Problem(models.Model):
    unit_id = models.IntegerField(default=1)
    question = models.CharField(max_length=50, null=True)
    expression = models.CharField(max_length=20, null=True)
    answer = models.IntegerField(blank=False, null=False)
    
    def __str__(self):
        return f'How to solve {self.expression}({self.answer}) (Unit {self.unit_id})'