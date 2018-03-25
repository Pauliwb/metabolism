# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

import django.utils.timezone
# Create your models here.


class Product(models.Model):
    name = models.CharField(unique=True, max_length=200)
    weight = models.IntegerField(default=0)
    caloricity = models.IntegerField(default=0)
    BGD = models.IntegerField(default=0)


class AppUser(models.Model):
    name = models.CharField(max_length=200)
    product = models.ManyToManyField(Product)


class UserInformation(models.Model):
    date = models.DateField(default=django.utils.timezone.now)
    appuser = models.OneToOneField(AppUser)