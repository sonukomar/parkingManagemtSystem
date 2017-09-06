# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class vehicle(models.Model):
    type  = models.CharField(max_length=10)


class user(models.Model):
    name  = models.CharField(max_length=40,blank=False, null=False)   
    email = models.EmailField(unique = True,blank=False, null=False)
    age   = models.IntegerField(max_length=3) 
    phone = models.IntegerField(max_length=3)

class cost(models.Model):
    currency = models.CharField(max_length=3)
    amount   = models.IntegerField()