# Generated by Django 4.2.8 on 2024-01-04 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_schedule_minischedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minischedule',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mini_schedule', to='courses.schedule'),
        ),
    ]