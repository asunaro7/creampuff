# Generated by Django 2.2.24 on 2021-08-26 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0018_auto_20210825_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='armorHead',
            field=models.ForeignKey(default='布の帽子', on_delete=django.db.models.deletion.PROTECT, to='todo.MyArmorHead', verbose_name='防具\u3000頭'),
        ),
        migrations.AlterField(
            model_name='user',
            name='armorLower',
            field=models.ForeignKey(default='衣下', on_delete=django.db.models.deletion.PROTECT, to='todo.MyArmorLower', verbose_name='防具\u3000下'),
        ),
        migrations.AlterField(
            model_name='user',
            name='armorUpper',
            field=models.ForeignKey(default='衣上', on_delete=django.db.models.deletion.PROTECT, to='todo.MyArmorUpper', verbose_name='防具\u3000上'),
        ),
        migrations.AlterField(
            model_name='user',
            name='hp',
            field=models.IntegerField(blank=True, default=100, null=True, verbose_name='HP'),
        ),
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='レベル'),
        ),
        migrations.AlterField(
            model_name='user',
            name='money',
            field=models.IntegerField(blank=True, default=1000, null=True, verbose_name='持ち金'),
        ),
        migrations.AlterField(
            model_name='user',
            name='weapon',
            field=models.ForeignKey(default='木刀', on_delete=django.db.models.deletion.PROTECT, to='todo.MyWeapon', verbose_name='武器'),
        ),
        migrations.AlterField(
            model_name='user2',
            name='armorHead',
            field=models.ForeignKey(default='布の帽子', on_delete=django.db.models.deletion.PROTECT, to='todo.MyArmorHead', verbose_name='防具\u3000頭'),
        ),
        migrations.AlterField(
            model_name='user2',
            name='armorLower',
            field=models.ForeignKey(default='衣下', on_delete=django.db.models.deletion.PROTECT, to='todo.MyArmorLower', verbose_name='防具\u3000下'),
        ),
        migrations.AlterField(
            model_name='user2',
            name='armorUpper',
            field=models.ForeignKey(default='衣上', on_delete=django.db.models.deletion.PROTECT, to='todo.MyArmorUpper', verbose_name='防具\u3000上'),
        ),
        migrations.AlterField(
            model_name='user2',
            name='hp',
            field=models.IntegerField(blank=True, default=100, null=True, verbose_name='HP'),
        ),
        migrations.AlterField(
            model_name='user2',
            name='level',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='レベル'),
        ),
        migrations.AlterField(
            model_name='user2',
            name='money',
            field=models.IntegerField(blank=True, default=1000, null=True, verbose_name='持ち金'),
        ),
        migrations.AlterField(
            model_name='user2',
            name='weapon',
            field=models.ForeignKey(default='木刀', on_delete=django.db.models.deletion.PROTECT, to='todo.MyWeapon', verbose_name='武器'),
        ),
    ]
