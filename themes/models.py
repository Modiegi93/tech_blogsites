#!/usr/bin/python3
from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=100)
    colors = models.CharField(max_length=100)
    font-family = models.CharField(max_length=100)
    font-size = models.PositiveIntegerField()

    def __str__(self):
        return self.name
