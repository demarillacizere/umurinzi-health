# Generated by Django 3.1.7 on 2021-02-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_auto_20210221_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='location',
            field=models.CharField(max_length=255),
        ),
    ]
