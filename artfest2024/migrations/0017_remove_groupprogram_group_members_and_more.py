# Generated by Django 4.2.4 on 2024-02-03 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artfest2024', '0016_remove_programs_max_number_of_people_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupprogram',
            name='group_members',
        ),
        migrations.AddField(
            model_name='groupprogram',
            name='group_members',
            field=models.ManyToManyField(to='artfest2024.studentdetails'),
        ),
    ]
