import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from api.service.create_profile import create_profile


class Position(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()


class Camera(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    name = models.TextField(null=True)


class Favorites(models.Model):
    name = models.TextField()
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)


class Profile(models.Model):
    name = models.TextField()
    surname = models.TextField()
    midname = models.TextField(default="")
    photo = models.ImageField(null=True)
    email = models.EmailField(max_length=254)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tel = models.TextField()


post_save.connect(create_profile, sender=User)


class History(models.Model):
    date = models.DateTimeField(datetime.datetime)
    file = models.FileField( null=True, blank=True)
