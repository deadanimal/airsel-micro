# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename


class OperationalReading(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset_id = models.CharField(max_length=100, default='NA')
    badge_number = models.CharField(max_length=100, default='NA')
    current_value = models.CharField(max_length=100, default='NA')
    measurent_identifier = models.CharField(max_length=100, default='NA')
    measurent_type = models.CharField(max_length=100, default='NA')
    initial_value_flag = models.CharField(max_length=100, default='NA')
    owning_organization = models.CharField(max_length=100, default='NA')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.asset_id


class WorkRequest(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=100, default='NA')
    long_description = models.TextField(max_length=512, default='NA')
    required_by_date = models.DateField(auto_now=True)
    approval_profile = models.CharField(max_length=100, default='NA')
    bo  = models.CharField(max_length=100, default='NA')

    downtime_start = models.DateTimeField(null=True)
    planner  = models.CharField(max_length=100, default='NA')
    work_class = models.CharField(max_length=100, default='NA')
    work_category = models.CharField(max_length=100, default='NA')
    work_priority = models.IntegerField(default=1)
    requestor = models.CharField(max_length=100, default='NA')
    owning_access_group = models.CharField(max_length=100, default='NA')
    first_name = models.CharField(max_length=100, default='NA')
    last_name = models.CharField(max_length=100, default='NA')
    primary_phone = models.CharField(max_length=100, default='NA')
    mobile_phone = models.CharField(max_length=100, default='NA')
    home_phone = models.CharField(max_length=100, default='NA')
    node_id = models.CharField(max_length=100, default='NA')
    asset_id = models.CharField(max_length=100, default='NA')

    created_by = models.CharField(max_length=100, default='NA')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.asset_id