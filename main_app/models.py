from django.db import models

# Create your models here.

class Zones(models.Model):
    name = models.CharField(max_length=30)
    superior_zone = models.ForeignKey("self")

class Cities(models.Model):
    name = models.CharField(max_length=30)
    zone = models.ForeignKey(Zones)

class Owners(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()

class Reviews(models.Model):
    text = models.TextField()
    date = models.DateTimeField('date published')
    hotel = models.ForeignKey("Hotels")
    author = models.CharField(max_length=30)
    grade = models.IntegerField()

class Hotels(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    facilities = models.TextField()
    location = models.TextField()
    city = models.ForeignKey(Cities)
    price = models.CharField(max_length=30)
    owner = models.ForeignKey(Owners)
