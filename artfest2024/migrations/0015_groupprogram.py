# Generated by Django 4.2.4 on 2024-02-03 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artfest2024', '0014_programs_max_number_of_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='group_program', to='artfest2024.programs')),
            ],
        ),
    ]
