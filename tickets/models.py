from django.db import models

# Create your models here.

# Create your models here.
# Guest- Movie - Reservation


class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=50)
    date = models.DateField()


class Guest(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
