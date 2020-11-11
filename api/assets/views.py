from django.shortcuts import render
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status
from rest_framework_extensions.mixins import NestedViewSetMixin

from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    AssetLocationCostCenter,
    AssetLocationCriticalityReason,
    AssetLocation,
    AssetMeasurementType,
    AssetAttribute,
    Asset
)

from .serializers import (
    AssetLocationCostCenterSerializer,
    AssetLocationCriticalityReasonSerializer,
    AssetLocationSerializer,
    AssetMeasurementTypeSerializer,
    AssetAttributeSerializer,
    AssetSerializer
)

class AssetLocationCostCenterViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AssetLocationCostCenter.objects.all()
    serializer_class = AssetLocationCostCenterSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = AssetLocationCostCenter.objects.all()

        """
        if self.request.user.is_anonymous:
            queryset = Company.objects.none()

        else:
            user = self.request.user
            company_employee = CompanyEmployee.objects.filter(employee=user)
            company = company_employee[0].company
            
            if company.company_type == 'AD':
                queryset = AssetLocationCostCenter.objects.all()
            else:
                queryset = AssetLocationCostCenter.objects.filter(company=company.id)
        """
        return queryset    
 
class AssetLocationCriticalityReasonViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AssetLocationCriticalityReason.objects.all()
    serializer_class = AssetLocationCriticalityReasonSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = AssetLocationCriticalityReason.objects.all()

        """
        if self.request.user.is_anonymous:
            queryset = Company.objects.none()

        else:
            user = self.request.user
            company_employee = CompanyEmployee.objects.filter(employee=user)
            company = company_employee[0].company
            
            if company.company_type == 'AD':
                queryset = AssetLocationCriticalityReason.objects.all()
            else:
                queryset = AssetLocationCriticalityReason.objects.filter(company=company.id)
        """
        return queryset    
 
class AssetLocationViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AssetLocation.objects.all()
    serializer_class = AssetLocationSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = AssetLocation.objects.all()

        """
        if self.request.user.is_anonymous:
            queryset = Company.objects.none()

        else:
            user = self.request.user
            company_employee = CompanyEmployee.objects.filter(employee=user)
            company = company_employee[0].company
            
            if company.company_type == 'AD':
                queryset = AssetLocation.objects.all()
            else:
                queryset = AssetLocation.objects.filter(company=company.id)
        """
        return queryset    
 
class AssetMeasurementTypeViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AssetMeasurementType.objects.all()
    serializer_class = AssetMeasurementTypeSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = AssetMeasurementType.objects.all()

        """
        if self.request.user.is_anonymous:
            queryset = Company.objects.none()

        else:
            user = self.request.user
            company_employee = CompanyEmployee.objects.filter(employee=user)
            company = company_employee[0].company
            
            if company.company_type == 'AD':
                queryset = AssetMeasurementType.objects.all()
            else:
                queryset = AssetMeasurementType.objects.filter(company=company.id)
        """
        return queryset    
 

class AssetAttributeViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AssetAttribute.objects.all()
    serializer_class = AssetAttributeSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = AssetAttribute.objects.all()

        """
        if self.request.user.is_anonymous:
            queryset = Company.objects.none()

        else:
            user = self.request.user
            company_employee = CompanyEmployee.objects.filter(employee=user)
            company = company_employee[0].company
            
            if company.company_type == 'AD':
                queryset = AssetAttribute.objects.all()
            else:
                queryset = AssetAttribute.objects.filter(company=company.id)
        """
        return queryset    
 

class AssetViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = Asset.objects.all()

        """
        if self.request.user.is_anonymous:
            queryset = Company.objects.none()

        else:
            user = self.request.user
            company_employee = CompanyEmployee.objects.filter(employee=user)
            company = company_employee[0].company
            
            if company.company_type == 'AD':
                queryset = Asset.objects.all()
            else:
                queryset = Asset.objects.filter(company=company.id)
        """
        return queryset    
 