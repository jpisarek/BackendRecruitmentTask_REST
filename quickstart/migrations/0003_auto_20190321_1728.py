# Generated by Django 2.0.13 on 2019-03-21 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_auto_20190320_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='grade',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.Task'),
        ),
    ]
