# Generated by Django 2.1.5 on 2022-11-03 04:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20221103_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 3, 4, 13, 23, 567296), editable=False),
        ),
    ]
