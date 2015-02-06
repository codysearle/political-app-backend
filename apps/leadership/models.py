from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Location(models.model):
    number = models.CharField(max_length=25, blank=True)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=12, blank=True)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class District(models.Model):
    location = models.ManyToMany(Location)

    def __str__(self):
        return self.name



class Politician(models.Model):
    name = models.Charfield(max_length=100)
    location = models.ManyToMany(Location)
    district = models.ManyToMany(District)


class Users(models.Model):
    name = models.OneToOneField(User)
    location = models.OneToOneField(Location)

    def __str__(self):
        return self.name
