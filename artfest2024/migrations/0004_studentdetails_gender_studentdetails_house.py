# Generated by Django 5.0.1 on 2024-01-17 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artfest2024', '0003_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='Gender',
            field=models.CharField(default='Male', max_length=20),
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='house',
            field=models.CharField(default='House 1', max_length=255),
        ),
    ]
