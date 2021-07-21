# Generated by Django 3.1.7 on 2021-07-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitCards', '0016_auto_20210721_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='facebook_link',
            field=models.TextField(default='facebook.com/', null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='website',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='whatsapp_link',
            field=models.TextField(default='', null=True),
        ),
    ]
