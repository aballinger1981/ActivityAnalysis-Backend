# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Athlete(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    profile_medium = models.URLField()
    profile = models.URLField()
    city = models.TextField()
    state = models.TextField()
    country = models.TextField()
    sex = models.CharField(max_length=1, null=True)
    email = models.EmailField()
    weight = models.DecimalField(max_digits=5, decimal_places=1)
    run_total = models.OneToOneField(RunTotal)
    ride_total = models.OneToOneField(RideTotal)
    swim_total = models.OneToOneField(SwimTotal)

class Bike(models.Model):
    athlete_id = models.ForeignKey(Athlete)
    name = models.TextField()
    distance = models.DecimalField(max_digits=None, decimal_places=2)
    primary = models.BooleanField()

class Shoe(models.Model):
    athlete_id = models.ForeignKey(Athlete)
    name = models.TextField()
    distance = models.DecimalField(max_digits=None, decimal_places=2)
    primary = models.BooleanField()

class RunTotal(models.Model):
    count = models.IntegerField()
    distance = models.IntegerField()
    moving_time = models.IntegerField()
    elapsed_time = models.IntegerField()
    elevation_game = models.IntegerField()

class RideTotal(models.Model):
    count = models.IntegerField()
    distance = models.IntegerField()
    moving_time = models.IntegerField()
    elapsed_time = models.IntegerField()
    elevation_game = models.IntegerField()

class SwimTotal(models.Model):
    count = models.IntegerField()
    distance = models.IntegerField()
    moving_time = models.IntegerField()
    elapsed_time = models.IntegerField()
    elevation_game = models.IntegerField()

class Activity(models.Model):
    athlete_id = models.ForeignKey(Athlete)
    name = models.TextField()
    description = models.TextField()
    distance = models.FloatField()
    moving_time = models.IntegerField()
    elapsed_time = models.IntegerField()
    total_elevation_gain = models.FloatField()
    elev_high = models.FloatField()
    elev_low = models.FloatField()
    activity_type = models.TextField()
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    start_date_local = models.DateTimeField(auto_now=False, auto_now_add=False)
    timezone = models.TextField()
    start_latlng = ArrayField(ArrayField(models.DecimalField(max_digits=None, decimal_places=6)))
    end_latlng = ArrayField(ArrayField(models.DecimalField(max_digits=None, decimal_places=6)))
    map_polyline = models.TextField()
    trainer = models.BooleanField()
    commute = models.BooleanField()
    manual = models.BooleanField()
    gear = models.OneToOneField(Gear)
    average_speed = models.FloatField()
    max_speed = models.FloatField()
    calories = models.FloatField()
    average_cadence = models.FloatField()

class Laps(models.Model):
    activity_id = models.ForeignKey(Activity)
    athlete_id = models.ForeignKey(Athlete)
    average_cadence = models.FloatField()
    average_speed = models.FloatField()
    distance = models.FloatField()
    elapsed_time = models.IntegerField()
    end_index = models.IntegerField()
    lap_index = models.IntegerField()
    max_speed = models.FloatField()
    moving_time = models.IntegerField()
    name = models.TextField()
    pace_zone = models.IntegerField()
    split = models.IntegerField()
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False))
    start_date_local = models.DateTimeField(auto_now=False, auto_now_add=False))
    start_index = models.IntegerField()
    total_elevation_gain = models.FloatField()

class Gear(models.Model):
    primary = models.BooleanField()
    name = models.TextField()
    distance = models.FloatField()

class SplitsMetric(models.Model):
    activity_id = models.ForeignKey(Activity)
    average_speed = models.FloatField()
    distance = models.FloatField()
    elapsed_time = models.IntegerField()
    elevation_difference = models.FloatField()
    moving_time = models.IntegerField()
    pace_zone = models.IntegerField()
    split = models.IntegerField()

  class SplitsStandard(models.Model):
    activity_id = models.ForeignKey(Activity)
    average_speed = models.FloatField()
    distance = models.FloatField()
    elapsed_time = models.IntegerField()
    elevation_difference = models.FloatField()
    moving_time = models.IntegerField()
    pace_zone = models.IntegerField()
    split = models.IntegerField()