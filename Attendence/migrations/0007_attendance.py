# Generated by Django 4.2.4 on 2024-01-28 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artfest2024', '0013_notification'),
        ('Attendence', '0006_delete_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_admn_no', models.CharField(default='', max_length=4)),
                ('period', models.IntegerField(choices=[(1, 'Period 1'), (2, 'Period 2'), (3, 'Period 3'), (4, 'Period 4'), (5, 'Period 5'), (6, 'Period 6')])),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('attendance', models.BooleanField()),
                ('co_ordinator', models.CharField(max_length=255)),
                ('program', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='artfest2024.programs')),
                ('stage', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Attendence.stage')),
            ],
        ),
    ]
