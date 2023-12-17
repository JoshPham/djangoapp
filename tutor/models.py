from django.db import models

class Grade(models.Model):
    grade_id = models.IntegerField(default=1)
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    units = models.ManyToManyField("Unit", related_name="related_grades")
    
    def __str__(self):
        return f'{self.title}'

class Unit(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name="related_units", default=1)
    unit_id = models.IntegerField(default=1)
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    problems = models.ManyToManyField("Problem", related_name="related_units")
    
    def __str__(self):
        return f'{self.title} ({self.grade.title})'

class Problem(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="related_problems", default=1)
    question = models.CharField(max_length=50, null=True)
    expression = models.CharField(max_length=20, null=True)
    answer = models.IntegerField(blank=False, null=False)
    
    def __str__(self):
        return f'{self.question} - {self.answer} (Unit {self.unit.unit_id}, {self.unit.grade.title})'
