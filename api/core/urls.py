from datetime import datetime, timedelta

from django.conf import settings
from django.conf.urls import include, url
from django.contrib.gis import admin

from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from users.views import (
    MyTokenObtainPairView
)

class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass

router = NestedDefaultRouter()

# Assets app
from assets.views import (
    AssetLocationViewSet,
    AssetMeasurementTypeViewSet,
    AssetAttributeViewSet,
    AssetViewSet
)

asset_locations_router = router.register(
    'asset-locations', AssetLocationViewSet
)

# asset_measurement_types_router = router.register(
#     'asset-measurement-types', AssetMeasurementTypeViewSet
# )

asset_attributes_router = router.register(
    'asset-attributes', AssetAttributeViewSet
)

assets_router = router.register(
    'assets', AssetViewSet
)

# Operations app

from operations.views import (
    OperationalReadingViewSet,
    WorkRequestViewSet,
    WorkOrderActivityViewSet,
    AssetLocationAssetListViewSet,
    ServiceHistoryViewSet,
    QuestionViewSet,
    ValidValueViewSet
)

operational_readings_router = router.register(
    'operational-readings', OperationalReadingViewSet
)

work_requests_router = router.register(
    'work-requests', WorkRequestViewSet
)

work_order_activities_router = router.register(
    'work-order-activities', WorkOrderActivityViewSet
)

# asset_location_asset_lists_router = router.register(
#     'asset-location-asset-lists', AssetLocationAssetListViewSet
# )

# service_histories_router = router.register(
#     'service-histories', ServiceHistoryViewSet
# )

# questions_router = router.register(
#     'questions', QuestionViewSet
# )

# valid_values_router = router.register(
#     'valid-values', ValidValueViewSet
# )

# Wams app

from wams.views import (
    WamsViewSet
)

wams_router = router.register(
    'wams', WamsViewSet
)

# Organisations app

from organisations.views import (
    OrganisationViewSet
)

organisations_router = router.register(
    'organisations', OrganisationViewSet
)

# Users app

from users.views import (
    CustomUserViewSet
)

users_router = router.register(
    'users', CustomUserViewSet
)

urlpatterns = [
    url(r'v1/', include(router.urls)),
    url(r'auth/', include('rest_auth.urls')),
    url(r'auth/registration/', include('rest_auth.registration.urls')),

    url('auth/obtain/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('auth/verify/', TokenVerifyView.as_view(), name='token_verify')
]