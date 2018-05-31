from __future__ import unicode_literals

from django.db import models
from datetime import date
from django.utils import timezone

class Student(models.Model):

    name = models.CharField(max_length=50)
    roll_no = models.IntegerField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)

    adhar_number = models.CharField(max_length=30, blank=True)
    mobile_number = models.IntegerField(blank=True, null=True)
    blood_group = models.CharField(max_length=30,blank=True, null=True)
    # photo_upload = models.ImageField(blank=True,null=True)

    # example_upload = models.FileField(blank=True,null=True)



