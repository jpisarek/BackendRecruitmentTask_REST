# Generated by Django 2.0.13 on 2019-03-22 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0010_auto_20190322_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allabout',
            name='task',
        ),
    ]
