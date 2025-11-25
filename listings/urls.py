from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ListingViewSet, BookingViewSet

router = DefaultRouter()
router.register('listings', ListingViewSet)
router.register('bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
