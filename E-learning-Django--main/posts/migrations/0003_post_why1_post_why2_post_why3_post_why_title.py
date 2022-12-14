# Generated by Django 4.1.3 on 2022-11-12 16:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_why_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='why1',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='why2',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='why3',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='why_title',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
