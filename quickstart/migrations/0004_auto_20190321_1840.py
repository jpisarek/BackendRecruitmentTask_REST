# Generated by Django 2.0.13 on 2019-03-21 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20190321_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
