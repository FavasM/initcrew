# Generated by Django 3.1.5 on 2021-01-19 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20210119_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='price',
            field=models.DecimalField(decimal_places=2, default=11.0, max_digits=1000),
        ),
    ]
