# Generated by Django 2.2.24 on 2021-07-23 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20210722_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='level',
            field=models.CharField(default='5', max_length=1, verbose_name='難易度'),
        ),
    ]
