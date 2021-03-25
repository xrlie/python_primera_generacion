from django.urls import path, include
from rest_framework import routers
from .views import OwnersViewSet, PetsViewSet, PetDatesViewSet

router = routers.DefaultRouter()
router.register(r'owners', OwnersViewSet)
router.register(r'pets', PetsViewSet)
router.register(r'petdates', PetDatesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]