# Generated by Django 4.0.6 on 2022-08-25 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0004_match_status1_match_status2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='room',
        ),
    ]
