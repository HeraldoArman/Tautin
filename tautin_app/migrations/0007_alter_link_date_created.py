# Generated by Django 5.0.6 on 2024-10-29 08:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tautin_app', '0006_alter_link_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 29, 8, 56, 27, 903151, tzinfo=datetime.timezone.utc)),
        ),
    ]