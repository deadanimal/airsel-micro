# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename


class AssetLocationCostCenter(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cost_center = models.CharField(max_length=100, default='NA')
    percentage = models.FloatField(default=0)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.cost_center

class AssetLocationCriticalityReason(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    criticality_reason = models.CharField(max_length=100, default='NA')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.criticality_reason

class AssetLocation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location_type = models.CharField(max_length=100, default='NA')
    locatin_disposition = models.CharField(max_length=100, default='NA')
    description = models.CharField(max_length=100, default='NA')
    parent_loc_or_org = models.CharField(max_length=100, default='NA')
    work_request_approval_profile = models.CharField(max_length=100, default='NA')
    owning_org = models.CharField(max_length=100, default='NA')
    
    building = models.CharField(max_length=100, default='NA')
    room = models.CharField(max_length=100, default='NA')
    position = models.CharField(max_length=100, default='NA')
    country = models.CharField(max_length=100, default='NA')
    address_1 = models.CharField(max_length=100, default='NA')
    address_2 = models.CharField(max_length=100, default='NA')
    address_3 = models.CharField(max_length=100, default='NA')
    cross_street = models.CharField(max_length=100, default='NA')
    city = models.CharField(max_length=100, default='NA')
    suburb = models.CharField(max_length=100, default='NA')
    state = models.CharField(max_length=100, default='NA')
    postal = models.CharField(max_length=100, default='NA')
    location_class = models.CharField(max_length=100, default='NA')
    
    main_contact = models.CharField(max_length=100, default='NA')
    maintenance_manager = models.CharField(max_length=100, default='NA')
    planner = models.CharField(max_length=100, default='NA')
    cost_center = models.ManyToManyField(AssetLocationCostCenter, blank=True, null=True)

    rcm_system = models.CharField(max_length=100, default='NA')
    environmental_rating = models.CharField(max_length=100, default='NA')
    service_condition = models.CharField(max_length=100, default='NA')
    duty_cycle = models.CharField(max_length=100, default='NA')
    backlog_group = models.CharField(max_length=100, default='NA')
    run_to_failure = models.CharField(max_length=100, default='NA')
    breaker = models.CharField(max_length=100, default='NA')
    runtime_source = models.CharField(max_length=100, default='NA')
    tag_number = models.CharField(max_length=100, default='NA')
    site_location = models.CharField(max_length=100, default='NA')
    point_id = models.CharField(max_length=100, default='NA')
    service_area = models.CharField(max_length=100, default='NA')
    latitude = models.CharField(max_length=100, default='NA')
    longitude = models.CharField(max_length=100, default='NA')
    asset_criticality = models.CharField(max_length=100, default='NA')
    criticality_reason = models.ManyToManyField(AssetLocationCriticalityReason, null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.work_request_approval_profile

class AssetMeasurementType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    measurement_type = models.CharField(max_length=100, default='NA')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.measurement_type


class AssetAttribute(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    characteristic_type = models.CharField(max_length=100, default='NA')
    adhoc_value = models.CharField(max_length=100, default='NA')
    characteristic_value = models.CharField(max_length=100, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.measurement_type


class Asset(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset_id = models.CharField(max_length=100, default='NA')
    asset_type = models.CharField(max_length=100, default='NA')
    transaction_type = models.CharField(max_length=100, default='NA')
    description = models.CharField(max_length=100, default='NA')
    bo = models.CharField(max_length=100, default='NA')
    bo_status = models.CharField(max_length=100, default='NA')
    owning_access_group = models.CharField(max_length=100, null=True, blank=True)
    effective_datetime = models.DateTimeField(auto_now=True)
    node_id = models.CharField(max_length=100, default='NA')
    badge_no = models.CharField(max_length=100, default='NA')
    serial_no = models.CharField(max_length=100, default='NA')
    pallet_no = models.CharField(max_length=100, default='NA')
    handed_over_asset = models.CharField(max_length=100, default='NA')
    fixed_asset_no = models.CharField(max_length=100, default='NA')
    scada_id = models.CharField(max_length=100, default='NA')
    condition_rating = models.CharField(max_length=100, default='NA')
    condifence_rating = models.CharField(max_length=100, default='NA')
    maintenance_specification = models.CharField(max_length=100, default='NA')
    measurement_types = models.ManyToManyField(AssetMeasurementType, null=True)
    bom_part_id = models.CharField(max_length=100, default='NA')
    attached_to_asset_id = models.CharField(max_length=100, default='NA')
    vehicle_identification_num = models.CharField(max_length=100, default='NA')
    license_number = models.CharField(max_length=100, default='NA')
    purchase_order_num = models.CharField(max_length=100, default='NA')
    location_id = models.CharField(max_length=100, default='NA')
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


