# Generated by Django 3.1.5 on 2021-01-12 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggers', '0003_bloggers_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloggers',
            name='short_description',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]