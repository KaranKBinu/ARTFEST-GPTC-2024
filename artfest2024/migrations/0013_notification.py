# Generated by Django 5.0.1 on 2024-01-25 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artfest2024', '0012_programs_show_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_shown', models.BooleanField(default=True)),
            ],
        ),
    ]