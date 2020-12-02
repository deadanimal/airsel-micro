from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.utils.timezone import now

from .models import (
    OperationalReading,
    WorkRequest,
    WorkOrderActivity,
    AssetLocationAssetList,
    ServiceHistory,
    Question,
    ValidValue
)

class OperationalReadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = OperationalReading
        fields = '__all__'

class WorkRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkRequest
        fields = '__all__'

class WorkOrderActivitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WorkOrderActivity
        fields = '__all__'

class AssetLocationAssetListSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssetLocationAssetList
        fields = '__all__'

class ServiceHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceHistory
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'

class ValidValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = ValidValue
        fields = '__all__'

class WorkOrderActivityExtendedSerializer(serializers.ModelSerializer):

    asset_location_asset_list_wo = AssetLocationAssetListSerializer(many=True)
    service_history_wo = ServiceHistorySerializer(many=True)
    question_wo = QuestionSerializer(many=True)
    valid_value_wo = ValidValueSerializer(many=True)

    class Meta:
        model = WorkOrderActivity
        fields = '__all__'
