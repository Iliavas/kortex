# Generated by Django 3.1.7 on 2021-08-03 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitCards', '0021_visitcard_inst_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitcard',
            name='is_inst_photos',
            field=models.BooleanField(default=False),
        ),
    ]