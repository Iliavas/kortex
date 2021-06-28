# Generated by Django 3.1.7 on 2021-06-14 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProfilePhoto', models.ImageField(null=True, upload_to='')),
                ('position_in_company', models.TextField(null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('second_descr', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('link', models.TextField(null=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitCards.visitcard')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitCards.visitcard')),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.TextField(null=True)),
                ('website', models.URLField(null=True)),
                ('tg_link', models.TextField(null=True)),
                ('whatsapp_link', models.TextField(null=True)),
                ('inst_link', models.TextField(null=True)),
                ('vk_link', models.TextField(null=True)),
                ('facebook_link', models.TextField(null=True)),
                ('twitter_link', models.TextField(null=True)),
                ('visit_card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='visitCards.visitcard')),
            ],
        ),
    ]
