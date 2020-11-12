from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
import datetime, pytz

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status
from rest_framework_extensions.mixins import NestedViewSetMixin

from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    OperationalReading,
    WorkRequest
)

from .serializers import (
    OperationalReadingSerializer,
    WorkRequestSerializer
)

class OperationalReadingViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = OperationalReading.objects.all()
    serializer_class = OperationalReadingSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = OperationalReading.objects.all()

        # FROM APPLICATION/JSON THROUGH API
        if bool(self.request.data):
            print("enter bool()")
            from_date = self.request.data['from_date']
            to_date = self.request.data['to_date']
            
            if from_date is not None and to_date is not None:
                # print(OperationalReading.objects.filter(created_date__range=(from_date,to_date)).query)
                queryset = OperationalReading.objects.filter(created_date__range=(from_date,to_date))

        return queryset    
 
class WorkRequestViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = WorkRequest.objects.all()
    serializer_class = WorkRequestSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = WorkRequest.objects.all()

        # FROM APPLICATION/JSON THROUGH API
        if bool(self.request.data):
            print("enter bool()")
            from_date = self.request.data['from_date']
            to_date = self.request.data['to_date']
            
            if from_date is not None and to_date is not None:
                # print(WorkRequest.objects.filter(created_date__range=(from_date,to_date)).query)
                queryset = WorkRequest.objects.filter(created_date__range=(from_date,to_date))

        return queryset    
 
