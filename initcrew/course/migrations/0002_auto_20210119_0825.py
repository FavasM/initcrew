# Generated by Django 3.1.5 on 2021-01-19 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='Author_name',
        ),
        migrations.AddField(
            model_name='courses',
            name='author_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
