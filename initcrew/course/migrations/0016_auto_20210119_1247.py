# Generated by Django 3.1.5 on 2021-01-19 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_courses_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='price',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]