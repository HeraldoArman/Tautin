# Generated by Django 5.0.6 on 2024-10-28 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tautin_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
