from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.core.files.storage import default_storage
from django.utils.timezone import make_aware

from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.conf import settings

import json
import base64

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status
from rest_framework_extensions.mixins import NestedViewSetMixin

from django_filters.rest_framework import DjangoFilterBackend

from datetime import datetime

from wams.services.int01_employee import get_employee
from wams.services.int02_workorderactivity import get_workorderactivity
from wams.services.int04_assetsyncoutbound import get_assetsyncoutbound
from wams.services.int08_failureprofile import get_failureprofile
from wams.services.int09_measurementtype import get_measurementtype
from wams.services.int11_planner import get_planner
from wams.services.int15_asset import get_asset
from wams.services.int19_maintenancemanager import get_maintenancemanager

from .models import (
    Wams
)

from .serializers import (
    WamsSerializer
)

class WamsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = Wams.objects.all()
    serializer_class = WamsSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        print('Version baru')
        queryset = Wams.objects.all()
        return queryset

    @action(methods=['POST'], detail=False)
    def services(self, request, *args, **kwargs):

        call_json = json.loads(request.body)
        request_service_name = call_json['service_name']

        if request_service_name == 'getEmployee':
            middleware_call = get_employee()
            # for single result only
            json_response = {
                'result': { k.replace('ouaf:', ''): v for k, v in middleware_call.items() }
            }

        elif request_service_name == 'getWorkOrderActivity':
            middleware_call = get_workorderactivity()
            # for multiple results only
            middleware_list = []
            for item in middleware_call:
                new_json = {}
                for key in item:
                    new_key = key.replace('ouaf:', '')
                    new_json[new_key] = item[key]
                middleware_list.append(new_json)
            
            json_response = {
                'result': middleware_list
            }

        elif request_service_name == 'getAssetSyncOutbound':
            middleware_call = get_assetsyncoutbound()
            
            middleware_list = []
            for item in middleware_call:
                new_json = {}
                for key in item:
                    new_key = key.replace('ouaf:', '')
                    new_json[new_key] = item[key]
                middleware_list.append(new_json)
            
            json_response = {
                'result': middleware_list
            }

        elif request_service_name == 'getFailureProfile':
            middleware_call = get_failureprofile()
            
            middleware_list = []
            for item in middleware_call:
                new_json = {}
                for key in item:
                    new_key = key.replace('ouaf:', '')
                    new_json[new_key] = item[key]
                middleware_list.append(new_json)
            
            json_response = {
                'result': middleware_list
            }

        elif request_service_name == 'getMeasurementType':
            middleware_call = get_measurementtype()
            
            middleware_list = []
            for item in middleware_call:
                new_json = {}
                for key in item:
                    new_key = key.replace('ouaf:', '')
                    new_json[new_key] = item[key]
                middleware_list.append(new_json)
            
            json_response = {
                'result': middleware_list
            }

        elif request_service_name == 'getPlanner':
            middleware_call = get_planner()

            middleware_list = []
            for item in middleware_call:
                new_json = {}
                for key in item:
                    new_key = key.replace('ouaf:', '')
                    new_json[new_key] = item[key]
                middleware_list.append(new_json)
            
            json_response = {
                'result': middleware_list
            }

        elif request_service_name == 'getAsset':
            middleware_call = get_asset()
            
            middleware_list = []
            for item in middleware_call:
                new_json = {}
                for key in item:
                    new_key = key.replace('ouaf:', '')
                    new_json[new_key] = item[key]
                middleware_list.append(new_json)
            
            json_response = {
                'result': middleware_list
            }

        elif request_service_name == 'getAssetLocation':
            middleware_call = get_asset()
            
            middleware_list = []
            for item in middleware_call:
                new_json = {}
                for key in item:
                    new_key = key.replace('ouaf:', '')
                    new_json[new_key] = item[key]
                middleware_list.append(new_json)
            
            json_response = {
                'result': middleware_list
            }

        elif request_service_name == 'getMaintenanceManager':
            middleware_call = get_maintenancemanager()
            
            middleware_list = []
            for item in middleware_call:
                new_json = {}
                for key in item:
                    new_key = key.replace('ouaf:', '')
                    new_json[new_key] = item[key]
                middleware_list.append(new_json)
            
            json_response = {
                'result': middleware_list
            }


        return JsonResponse(json_response)
