# Generated by Django 3.1.7 on 2021-06-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vdapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='thumbnail',
            field=models.FileField(upload_to='video/%y'),
        ),
    ]
