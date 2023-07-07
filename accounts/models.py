#!/usr/bin/python3
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Additional fields"""
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username
