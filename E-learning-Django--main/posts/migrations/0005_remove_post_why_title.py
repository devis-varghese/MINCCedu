# Generated by Django 4.1.3 on 2022-11-12 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_post_why1_remove_post_why2_remove_post_why3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='why_title',
        ),
    ]
