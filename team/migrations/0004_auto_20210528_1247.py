# Generated by Django 3.1.7 on 2021-05-28 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_auto_20210528_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='facebook',
            field=models.URLField(blank=True, default='#!', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='linkedin',
            field=models.URLField(blank=True, default='#!', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='twitter',
            field=models.URLField(blank=True, default='#!', null=True),
        ),
    ]
