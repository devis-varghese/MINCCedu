# Generated by Django 4.1.3 on 2022-11-12 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_remove_post_maincourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='hit',
        ),
    ]