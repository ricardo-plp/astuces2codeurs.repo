# Generated by Django 4.2.3 on 2023-07-29 21:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 29, 21, 28, 50, 789517, tzinfo=datetime.timezone.utc)),
        ),
    ]