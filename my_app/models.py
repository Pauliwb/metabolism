# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

import django.utils.timezone
# Create your models here.


class Product(models.Model):
    class Meta():
        db_table="product"
    name = models.CharField(unique=True, max_length=200)
    weight = models.IntegerField(default=0)
    caloricity = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    carbohydrate = models.IntegerField(default=0)


class AppUser(models.Model):
    class Meta():
        db_table="appuser"
    name = models.CharField(max_length=200)
    product = models.ManyToManyField(Product)


class UserInformation(models.Model):
    class Meta():
        db_table="useronfo"
    date = models.DateField(default=django.utils.timezone.now)
    weight = models.IntegerField(default=0)
    appuser = models.OneToOneField(AppUser)