# Generated by Django 4.2.7 on 2023-12-16 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50, null=True)),
                ('expression', models.CharField(max_length=20)),
                ('answer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_number', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor.problem')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor.unit')),
            ],
        ),
    ]
