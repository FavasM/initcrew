# Generated by Django 3.1.5 on 2021-01-19 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_courses_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=1000),
        ),
    ]
