# Generated by Django 2.2.24 on 2021-08-11 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_remove_todo_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attack', models.PositiveIntegerField(default=0, verbose_name='攻撃力')),
            ],
        ),
    ]
