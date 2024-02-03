# Generated by Django 4.2.4 on 2024-02-03 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artfest2024', '0015_groupprogram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programs',
            name='max_number_of_people',
        ),
        migrations.AddField(
            model_name='groupprogram',
            name='group_leader',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AddField(
            model_name='groupprogram',
            name='group_members',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='group_members', to='artfest2024.studentdetails'),
        ),
        migrations.AddField(
            model_name='groupprogram',
            name='max_number_of_people',
            field=models.IntegerField(default=1),
        ),
    ]