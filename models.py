

from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Timmy(models.Model):
    name = models.CharField(max_length=60)
    date = models.DateField
    def __str__(self):
        return self.name

class Actors(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    experience = models.IntegerField()
    headshot = models.ImageField()


