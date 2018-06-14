# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name

class TestCase(models.Model):
    case_name = models.CharField(max_length=64,unique=True)
    add_time = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=64, default="work.1688.com")

    def __unicode__(self):
        return self.case_name

class TestCaseStep(models.Model):
    step_name = models.CharField(max_length=64,unique=True)
    add_time = models.DateTimeField(auto_now_add=True)
    case_name = models.CharField(max_length=64)
    case_id = models.IntegerField(auto_created=1)
    step_order = models.IntegerField()
    locator = models.CharField(max_length=64)
    location = models.CharField(max_length=256)
    type = models.CharField(max_length=64)
    element_type = models.CharField(max_length=64)
    ops = models.CharField(max_length=64)
    value = models.CharField(max_length=1024)
    reg_type = models.CharField(max_length=1024)
    ret_assert = models.CharField(max_length=256)
    required = models.IntegerField()
    ops_detail = models.CharField(max_length=64)
    pic_address = models.CharField(max_length=256)
    imgdiff = models.IntegerField()
    
    def __unicode__(self):
        return self.step_name