# Generated by Django 3.1.4 on 2021-01-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sliders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headlines', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='media/slider/%Y/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
