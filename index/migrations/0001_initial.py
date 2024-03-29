# Generated by Django 4.0.5 on 2022-08-14 03:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='stocks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nameofstocks', models.CharField(max_length=30)),
                ('buy', models.IntegerField(blank=True, default=0, null=True)),
                ('buydate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('sell', models.IntegerField(blank=True, default=0, null=True)),
                ('selldate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('t1', models.IntegerField(blank=True, default=0, null=True)),
                ('t2', models.IntegerField(blank=True, default=0, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
