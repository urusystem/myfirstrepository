# Generated by Django 3.0 on 2020-05-30 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscapp', '0005_subsc_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsc',
            name='period',
            field=models.IntegerField(default=0),
        ),
    ]
