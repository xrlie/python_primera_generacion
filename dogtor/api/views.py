from django.shortcuts import render

from rest_framework import viewsets

from vet.models import PetOwner, Pet, PetDate
from .serializers import OwnersSerializer, PetsSerializer
from .serializers import PetDatesSerializer

# Create your views here.
class OwnersViewSet(viewsets.ModelViewSet) :
    """ Viewset del modelo PetOwners """

    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class PetsViewSet(viewsets.ModelViewSet) :
    """ Viewset del modelo Pet """

    queryset = Pet.objects.all().order_by('created_at')
    serializer_class = PetsSerializer

class PetDatesViewSet(viewsets.ModelViewSet) :
    """ Viewset del modelo PetDate """

    queryset = PetDate.objects.all()
    serializer_class = PetDatesSerializer