# Generated by Django 4.2.7 on 2023-12-16 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0002_remove_grade_unit_remove_unit_problem_grade_unit_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='unit_number',
            new_name='unit_id',
        ),
    ]