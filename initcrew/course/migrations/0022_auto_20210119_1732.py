# Generated by Django 3.1.5 on 2021-01-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0021_auto_20210119_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='videoindroduction',
            field=models.FileField(blank=True, upload_to='initcrew/static/course_video/%Y/'),
        ),
    ]
