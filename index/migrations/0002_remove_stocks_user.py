# Generated by Django 4.0.5 on 2022-08-14 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocks',
            name='user',
        ),
    ]
