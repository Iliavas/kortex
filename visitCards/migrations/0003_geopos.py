# Generated by Django 3.1.7 on 2021-06-14 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitCards', '0002_auto_20210615_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoPos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lattitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='visitCards.visitcard')),
            ],
        ),
    ]