# Generated by Django 4.2.7 on 2023-12-17 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0009_remove_problem_unit_id_remove_unit_grade_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='expression',
        ),
    ]
