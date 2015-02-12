from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password, is_password_usable


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """Creates a token whenever a User is created"""
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def hash_password(sender, instance=None, created=False, **kwargs):
   ''' Hashes the password given when a User is created or updated '''
   if not is_password_usable(instance.password):
       instance.password = make_password(instance.password)
       instance.save()

class Zipcode(models.Model):
    zip_code = models.CharField(max_length=10)

class Location(models.Model):
    number = models.CharField(max_length=25, blank=True)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=12, blank=True)
    zip_code = models.ManyToManyField(Zipcode)

    def __str__(self):
        return self.name


class District(models.Model):
    location = models.ManyToManyField(Location)

    def __str__(self):
        return self.name



class Politician(models.Model):
    name = models.CharField(max_length=100)
    location = models.ManyToManyField(Location)
    district = models.ManyToManyField(District)


class Users(models.Model):
    name = models.OneToOneField(User)
    location = models.OneToOneField(Location)

    def __str__(self):
        return self.name
