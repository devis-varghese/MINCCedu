# Generated by Django 4.1.3 on 2022-11-12 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_remove_timing_time_duration1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timing',
            name='time_duration1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
