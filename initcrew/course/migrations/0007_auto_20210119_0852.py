# Generated by Django 3.1.5 on 2021-01-19 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20210119_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='short_description',
            field=models.TextField(blank=True, max_length=1200),
        ),
    ]
