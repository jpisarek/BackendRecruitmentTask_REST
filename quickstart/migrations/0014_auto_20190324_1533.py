# Generated by Django 2.0.13 on 2019-03-24 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0013_delete_snippet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allabout',
            name='candidate',
        ),
        migrations.RemoveField(
            model_name='allabout',
            name='grades',
        ),
        migrations.DeleteModel(
            name='AllAbout',
        ),
    ]