# Django Practice
This is my practice for my TSA Project for Software Design. This is a math tutor for grades K-5

## Additional Info
If you are trying to pull from this repository, and want to import some example grades, units, and problems, you can use the following code statements in a python shell:

```{python}
grade_instance = Grade.objects.create(title='1st Grade', description='Introduction to addition and subtraction')
unit_instance = Unit.objects.create(grade=grade_instance, unit_id=1, title='Unit 1', description='Intro to adding')
problem_instance = Problem.objects.create(unit=unit_instance, question='What is 2 + 2?', expression='2 + 2', answer=4)