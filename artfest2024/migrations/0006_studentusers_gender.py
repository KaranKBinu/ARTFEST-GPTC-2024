# Generated by Django 5.0.1 on 2024-01-17 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artfest2024', '0005_programs_alter_studentdetails_house_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentusers',
            name='Gender',
            field=models.CharField(default='', max_length=20),
        ),
    ]
