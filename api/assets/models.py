# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename

from jsonfield import JSONField

class AssetLocation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location_type = models.CharField(max_length=100)
    locatin_disposition = models.CharField(max_length=100)
    bo = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    parent_loc_or_org = models.CharField(max_length=100)
    work_request_approval_profile = models.CharField(max_length=100)
    owning_org = models.CharField(max_length=100)
    
    building = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    address_3 = models.CharField(max_length=100)
    cross_street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    suburb = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal = models.CharField(max_length=100)
    location_class = models.CharField(max_length=100)
    
    main_contact = models.CharField(max_length=100)
    maintenance_manager = models.CharField(max_length=100)
    planner = models.CharField(max_length=100)
    cost_center = models.CharField(max_length=100, blank=True, null=True)
    percentage = models.FloatField(default=0)

    rcm_system = models.CharField(max_length=100)
    environmental_rating = models.CharField(max_length=100)
    service_condition = models.CharField(max_length=100)
    duty_cycle = models.CharField(max_length=100)
    backlog_group = models.CharField(max_length=100)
    run_to_failure = models.CharField(max_length=100)
    breaker = models.CharField(max_length=100)
    runtime_source = models.CharField(max_length=100)
    tag_number = models.CharField(max_length=100)
    site_location = models.CharField(max_length=100)
    point_id = models.CharField(max_length=100)
    service_area = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    asset_criticality = models.CharField(max_length=100)
    criticality_reason = models.CharField(max_length=100)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.work_request_approval_profile

class AssetMeasurementType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    measurement_type = models.CharField(max_length=100, null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.measurement_type


class AssetAttribute(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    characteristic_type = models.CharField(max_length=100, null=True, blank=True)
    adhoc_value = models.CharField(max_length=100, null=True, blank=True)
    characteristic_value = models.CharField(max_length=100, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.measurement_type


class Asset(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset_id = models.CharField(max_length=100, null=True, blank=True)
    asset_type = models.CharField(max_length=100, null=True, blank=True)
    transaction_type = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    bo = models.CharField(max_length=100, null=True, blank=True)
    bo_status = models.CharField(max_length=100, null=True, blank=True)
    owning_access_group = models.CharField(max_length=100, null=True, blank=True)
    effective_datetime = models.DateTimeField(auto_now=True)
    node_id = models.CharField(max_length=100, null=True, blank=True)
    badge_no = models.CharField(max_length=100, null=True, blank=True)
    serial_no = models.CharField(max_length=100, null=True, blank=True)
    pallet_no = models.CharField(max_length=100, null=True, blank=True)
    handed_over_asset = models.CharField(max_length=100, null=True, blank=True)
    fixed_asset_no = models.CharField(max_length=100, null=True, blank=True)
    scada_id = models.CharField(max_length=100, null=True, blank=True)
    condition_rating = models.CharField(max_length=100, null=True, blank=True)
    condifence_rating = models.CharField(max_length=100, null=True, blank=True)
    maintenance_specification = models.CharField(max_length=100, null=True, blank=True)
    measurement_types = JSONField(null=True)
    bom_part_id = models.CharField(max_length=100, null=True, blank=True)
    attached_to_asset_id = models.CharField(max_length=100, null=True, blank=True)
    vehicle_identification_num = models.CharField(max_length=100, null=True, blank=True)
    license_number = models.CharField(max_length=100, null=True, blank=True)
    purchase_order_num = models.CharField(max_length=100, null=True, blank=True)
    location_id = models.CharField(max_length=100, null=True, blank=True)
    metrology_firmware = models.CharField(max_length=100, default='NA')
    nic_firmware = models.CharField(max_length=100, default='NA')
    configuration = models.CharField(max_length=100, default='NA')
    warranty_expiration_date = models.DateField(null=True)
    warranty_detail = models.CharField(max_length=100, default='NA')
    vendor_part_no = models.CharField(max_length=100, default='NA')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.asset_id


