# Generated by Django 3.1.7 on 2021-02-22 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0006_auto_20210222_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='located_at',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to='health.location'),
        ),
    ]