# Generated by Django 2.2.5 on 2020-10-06 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0008_auto_20201005_0701'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
                ('rooms', models.ManyToManyField(related_name='lists', to='rooms.Room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
