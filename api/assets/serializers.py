from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.utils.timezone import now

from .models import (
    AssetLocation,
    AssetMeasurementType,
    AssetAttribute,
    Asset
)

class AssetLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssetLocation
        fields = '__all__'

class AssetMeasurementTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssetMeasurementType
        fields = '__all__'

class AssetAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssetAttribute
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset
        fields = '__all__'