# Generated by Django 5.0.1 on 2024-01-16 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artfest2024', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255)),
                ('admn_no', models.IntegerField()),
                ('branch', models.CharField(max_length=50)),
                ('sem', models.CharField(max_length=10)),
            ],
        ),
    ]
