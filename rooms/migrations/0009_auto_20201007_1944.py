# Generated by Django 2.2.5 on 2020-10-07 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_auto_20201005_0701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='guestes',
            new_name='guests',
        ),
    ]
