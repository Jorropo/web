# Generated by Django 2.2.4 on 2020-06-01 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0117_hackathonevent_short_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathonproject',
            name='winner',
            field=models.BooleanField(default=False),
        ),
    ]
