# Generated by Django 4.1.3 on 2022-11-12 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_post_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='old_price',
        ),
    ]