# Generated by Django 2.2 on 2021-09-27 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210927_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='created_at',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]