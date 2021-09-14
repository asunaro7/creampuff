# Generated by Django 2.2.24 on 2021-07-21 10:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20210721_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created_at',
        ),
        migrations.AddField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
