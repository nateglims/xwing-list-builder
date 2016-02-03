from __future__ import unicode_literals

from django.db import models


class Ship(models.Model):
    name = models.CharField(max_length=256)
    stats = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class List(models.Model):
    name = models.CharField(max_length=256)
    max_points = models.IntegerField(default=100)
    ships = models.ManyToManyField(Ship, through='ListShipInclusion')

    def __str__(self):
        return self.name


class ListShipInclusion(models.Model):
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    xlist = models.ForeignKey(List, on_delete=models.CASCADE)
