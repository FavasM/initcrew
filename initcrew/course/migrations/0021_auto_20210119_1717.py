# Generated by Django 3.1.5 on 2021-01-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0020_courses_videoindroduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='notification_link',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='courses',
            name='resources_link',
            field=models.CharField(blank=True, max_length=155),
        ),
    ]
