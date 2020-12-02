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
    WorkRequest,
    WorkOrderActivity,
    AssetLocationAssetList,
    ServiceHistory,
    Question,
    ValidValue
)

from .serializers import (
    OperationalReadingSerializer,
    WorkRequestSerializer,
    WorkOrderActivitySerializer,
    WorkOrderActivityExtendedSerializer,
    AssetLocationAssetListSerializer,
    ServiceHistorySerializer,
    QuestionSerializer,
    ValidValueSerializer
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
 

class WorkOrderActivityViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = WorkOrderActivity.objects.all()
    serializer_class = WorkOrderActivitySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = WorkOrderActivity.objects.all()

        if bool(self.request.data):
            # print('test')
            if 'from_date' in self.request.data:
                # print('ada')
                from_date = self.request.data['from_date']
                to_date = self.request.data['to_date']
                
                if from_date is not None and to_date is not None:
                    # print(AssetLocation.objects.filter(created_date__range=(from_date,to_date)).query)
                    queryset = WorkOrderActivity.objects.filter(created_date__range=(from_date,to_date))

        return queryset    
    
    @action(methods=['GET'], detail=False)
    def extended_all(self, request, *args, **kwargs):  
        queryset = WorkOrderActivity.objects.all()
        serializer = WorkOrderActivityExtendedSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(methods=['GET'], detail=True)
    def extended(self, request, *args, **kwargs):  

        work_order_activity = self.get_object()

        serializer = WorkOrderActivityExtendedSerializer(work_order_activity)
        return Response(serializer.data)
 

class AssetLocationAssetListViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AssetLocationAssetList.objects.all()
    serializer_class = AssetLocationAssetListSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = AssetLocationAssetList.objects.all()

        if bool(self.request.data):
            if 'from_date' in self.request.data:
                from_date = self.request.data['from_date']
                to_date = self.request.data['to_date']
                
                if from_date is not None and to_date is not None:
                    # print(AssetLocation.objects.filter(created_date__range=(from_date,to_date)).query)
                    queryset = AssetLocationAssetList.objects.filter(created_date__range=(from_date,to_date))
                
        return queryset    
 

class ServiceHistoryViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = ServiceHistory.objects.all()

        if bool(self.request.data):
            if 'from_date' in self.request.data:
                from_date = self.request.data['from_date']
                to_date = self.request.data['to_date']
                
                if from_date is not None and to_date is not None:
                    # print(AssetLocation.objects.filter(created_date__range=(from_date,to_date)).query)
                    queryset = ServiceHistory.objects.filter(created_date__range=(from_date,to_date))
                
        return queryset    
 

class QuestionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = Question.objects.all()

        if bool(self.request.data):
            if 'from_date' in self.request.data:
                from_date = self.request.data['from_date']
                to_date = self.request.data['to_date']
                
                if from_date is not None and to_date is not None:
                    # print(AssetLocation.objects.filter(created_date__range=(from_date,to_date)).query)
                    queryset = Question.objects.filter(created_date__range=(from_date,to_date))

        return queryset    
 

class ValidValueViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = ValidValue.objects.all()
    serializer_class = ValidValueSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = ValidValue.objects.all()

        if bool(self.request.data):
            if 'from_date' in self.request.data:
                from_date = self.request.data['from_date']
                to_date = self.request.data['to_date']
                
                if from_date is not None and to_date is not None:
                    # print(AssetLocation.objects.filter(created_date__range=(from_date,to_date)).query)
                    queryset = ValidValue.objects.filter(created_date__range=(from_date,to_date))

        return queryset    
 