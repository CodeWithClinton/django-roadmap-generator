# Generated by Django 4.2.8 on 2024-01-09 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_quiz_quizoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizoption',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='courses.quiz'),
        ),
    ]
