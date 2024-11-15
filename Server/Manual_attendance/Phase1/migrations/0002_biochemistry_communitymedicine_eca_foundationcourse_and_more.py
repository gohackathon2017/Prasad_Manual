# Generated by Django 5.1.1 on 2024-10-27 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Phase1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biochemistry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(editable=False, max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')], max_length=1)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phase1.phase1student')),
            ],
            options={
                'unique_together': {('roll_number', 'date')},
            },
        ),
        migrations.CreateModel(
            name='CommunityMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(editable=False, max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')], max_length=1)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phase1.phase1student')),
            ],
            options={
                'unique_together': {('roll_number', 'date')},
            },
        ),
        migrations.CreateModel(
            name='ECA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(editable=False, max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')], max_length=1)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phase1.phase1student')),
            ],
            options={
                'unique_together': {('roll_number', 'date')},
            },
        ),
        migrations.CreateModel(
            name='FoundationCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(editable=False, max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')], max_length=1)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phase1.phase1student')),
            ],
            options={
                'unique_together': {('roll_number', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Physicology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(editable=False, max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')], max_length=1)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phase1.phase1student')),
            ],
            options={
                'unique_together': {('roll_number', 'date')},
            },
        ),
    ]
