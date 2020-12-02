# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename

from jsonfield import JSONField

class OperationalReading(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset_id = models.CharField(max_length=100)
    badge_number = models.CharField(max_length=100)
    current_value = models.CharField(max_length=100)
    measurent_identifier = models.CharField(max_length=100)
    measurent_type = models.CharField(max_length=100)
    
    VALUE_FLAG = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    initial_value_flag = models.CharField(choices=VALUE_FLAG, max_length=1, default='Y')
    owning_organization = models.CharField(max_length=100)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.asset_id


class WorkRequest(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=100)
    long_description = models.TextField(max_length=512)
    required_by_date = models.DateField(auto_now=True)
    approval_profile = models.CharField(max_length=100)
    bo = models.CharField(max_length=100)

    downtime_start = models.DateTimeField(null=True)
    planner  = models.CharField(max_length=100)
    work_class = models.CharField(max_length=100)
    work_category = models.CharField(max_length=100)
    work_priority = models.IntegerField(default=1)
    requestor = models.CharField(max_length=100)
    owning_access_group = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    primary_phone = models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=100)
    home_phone = models.CharField(max_length=100)
    node_id = models.CharField(max_length=100)
    asset_id = models.CharField(max_length=100)

    created_by = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.asset_id

class WorkOrderActivity(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    activity_id = models.CharField(max_length=100)
    completion_datetime = models.DateTimeField()
    response = models.CharField(max_length=100)
    response_checkbox = models.CharField(max_length=100)
    response_radio = models.CharField(max_length=100)
    response_date = models.CharField(max_length=100)
    reading_datetime = models.CharField(max_length=100)

    measurement_type = models.CharField(max_length=100)
    reading_type = models.CharField(max_length=100)
    reading_datetime = models.DateTimeField(null=True)
    current_value = models.CharField(max_length=100)

    asset_location_asset_list = JSONField(null=True)
    service_histories = JSONField(null=True)
    questions = JSONField(null=True)
    valid_values = JSONField(null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.activity_id

class AssetLocationAssetList(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    work_order = models.ForeignKey(WorkOrderActivity, related_name='asset_location_asset_list_wo', on_delete=models.CASCADE)
    node_id = models.CharField(max_length=100)
    asset_id = models.CharField(max_length=100)
    participant = models.CharField(max_length=100)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.asset_id

class ServiceHistory(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    work_order = models.ForeignKey(WorkOrderActivity, related_name='service_history_wo', on_delete=models.CASCADE)
    service_history_type = models.CharField(max_length=100)
    effective_datetime = models.DateTimeField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    comments = models.CharField(max_length=100)

    failure_type = models.CharField(max_length=100)
    failure_mode = models.CharField(max_length=100)
    failure_repair = models.CharField(max_length=100)
    failure_component = models.CharField(max_length=100)
    failure_root_cause = models.CharField(max_length=100)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.service_history_type

class Question(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    work_order = models.ForeignKey(WorkOrderActivity, related_name='question_wo', on_delete=models.CASCADE)

    seq = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    short_text = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    tyle = models.CharField(max_length=100)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.code

class ValidValue(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    work_order = models.ForeignKey(WorkOrderActivity, related_name='valid_value_wo', on_delete=models.CASCADE)

    seq = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    short_text = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    tyle = models.CharField(max_length=100)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.code