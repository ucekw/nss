# Generated by Django 5.1 on 2024-09-30 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceVolunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.attendanceevent')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.attendancevolunteer')),
            ],
            options={
                'unique_together': {('volunteer', 'event', 'date')},
            },
        ),
    ]
