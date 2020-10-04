# Generated by Django 2.2.5 on 2020-10-04 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20201004_0512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='room',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]