# Generated by Django 3.1.5 on 2021-01-19 17:08

from django.db import migrations
import private_storage.fields
import private_storage.storage.files


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0025_auto_20210119_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='videoindroduction',
            field=private_storage.fields.PrivateFileField(storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to='uploads', verbose_name='file'),
        ),
    ]
