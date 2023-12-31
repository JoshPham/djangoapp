# Generated by Django 4.2.7 on 2023-12-17 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0007_alter_problem_expression'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='unit',
        ),
        migrations.AddField(
            model_name='grade',
            name='grade_id',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='grade',
            name='units',
            field=models.ManyToManyField(limit_choices_to={'grade_id__icontains': models.IntegerField(default=3)}, to='tutor.unit'),
        ),
        migrations.AddField(
            model_name='unit',
            name='grade_id',
            field=models.IntegerField(default=3),
        ),
    ]
