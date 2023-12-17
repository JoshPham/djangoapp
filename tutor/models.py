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
        return f'{self.grade.title}: Unit {self.unit_id} - {self.title}'

class Problem(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="related_problems", default=1)
    group = models.IntegerField(default=1)
    question = models.CharField(max_length=50, null=True, blank=True)
    question_image = models.ImageField(upload_to='images/', null=True, blank=True)
    int_answer = models.IntegerField(null=True, blank=True)
    text_answer1 = models.CharField(max_length=20, blank=True, null=True)
    text_answer2 = models.CharField(max_length=20, blank=True, null=True)
    answer_image1 = models.ImageField(upload_to='images/', blank=True, null=True)
    answer_image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return f'{self.question} (Unit {self.unit.unit_id}, {self.unit.grade.title})'
