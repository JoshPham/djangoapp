# Generated by Django 4.2.7 on 2023-12-16 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='problem',
        ),
        migrations.AddField(
            model_name='grade',
            name='unit',
            field=models.ManyToManyField(to='tutor.unit'),
        ),
        migrations.AddField(
            model_name='unit',
            name='problem',
            field=models.ManyToManyField(to='tutor.problem'),
        ),
    ]
