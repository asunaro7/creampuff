# Generated by Django 2.2.24 on 2021-08-11 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_game_monster_hp'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
