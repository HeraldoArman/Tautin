# Generated by Django 5.0.6 on 2024-11-08 06:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tautin_app', '0016_alter_link_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 8, 6, 14, 26, 884209, tzinfo=datetime.timezone.utc)),
        ),
    ]