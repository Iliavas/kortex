from django.db import models

from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save


class VisitCard(models.Model):
    ProfilePhoto = models.ImageField(null=True)
    name = models.TextField(null=True)
    surname = models.TextField(default="")
    midname = models.TextField(default="")
    position_in_company = models.TextField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=200, null=True)
    second_descr = models.CharField(null=True, max_length=200)

    project_descr = models.TextField(default="Мои проекты: ")
    geo_descr = models.TextField(default="Мой офис: ")
    photo_descr = models.TextField(default="Мои фото: ")

    theme = models.TextField(default="Dark")


class Contacts(models.Model):
    phone = models.TextField(null=True)
    website = models.URLField(null=True)
    tg_link = models.TextField(null=True)
    whatsapp_link = models.TextField(null=True)
    inst_link = models.TextField(null=True)
    vk_link = models.TextField(null=True)
    facebook_link = models.TextField(null=True)
    twitter_link = models.TextField(null=True)

    visit_card = models.OneToOneField(VisitCard, on_delete=models.CASCADE)


class Project(models.Model):
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    link = models.TextField(null=True)
    card = models.ForeignKey(VisitCard, on_delete=models.CASCADE)


class Photo(models.Model):
    image = models.ImageField()
    card = models.ForeignKey(VisitCard, on_delete=models.CASCADE, null=True)


class GeoPos(models.Model):
    lattitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    card = models.OneToOneField(VisitCard, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_empty_visit_card(**kwargs):
    user_instance = kwargs.get("instance")

    visit_card = VisitCard.objects.create(user=user_instance)
    Contacts.objects.create(visit_card=visit_card)
    GeoPos.objects.create(card=visit_card)