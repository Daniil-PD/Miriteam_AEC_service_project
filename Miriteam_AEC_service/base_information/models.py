from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Event(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    organizer = models.CharField(max_length=250)


# class Team(models.Model):
#     name = models.CharField(max_length=255)
#     users = models.ManyToManyField(User)


class Program(models.Model):
    name = models.CharField(max_length=255)
    direction = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)


class Information(models.Model):
    text = models.TextField()
    vector = ArrayField(base_field=models.FloatField())

