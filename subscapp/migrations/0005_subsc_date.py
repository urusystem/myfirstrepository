# Generated by Django 3.0 on 2020-05-30 12:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subscapp', '0004_remove_subsc_validation'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsc',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]