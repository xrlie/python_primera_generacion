from django.shortcuts import render

from rest_framework import generics # viewsets

from vet.models import PetOwner, Pet, PetDate

from .serializers import OwnersListSerializer, OwnersSerializer
from .serializers import PetsListSerializer, PetsSerializer

# Relations serializers
from .serializers import (
    OwnerPetsSerializer,
    PetOwnerSerializer,
    PetDatesSerializer,
)
# from .serializers import OwnersSerializer, PetsSerializer
# from .serializers import PetDatesSerializer

# # Create your views here.

# Generic Views
## Owners Views
class ListOwnersAPIView(generics.ListAPIView) :
    queryset = PetOwner.objects.all().order_by('created_at')
    serializer_class = OwnersListSerializer

class CreateOwnersAPIView(generics.CreateAPIView) :
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class RetrieveOwnersAPIView(generics.RetrieveAPIView) :
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class UpdateOwnersAPIView(generics.UpdateAPIView) :
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class DestroyOwnersAPIView(generics.DestroyAPIView) :
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

## Pets Views
class ListPetsAPIView(generics.ListAPIView) :
    queryset = Pet.objects.all().order_by('created_at')
    serializer_class = PetsListSerializer

class CreatePetsAPIView(generics.CreateAPIView) :
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class RetrievePetsAPIView(generics.RetrieveAPIView) :
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class UpdatePetsAPIView(generics.UpdateAPIView) :
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class DestroyPetsAPIView(generics.DestroyAPIView) :
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

## Relations
class RetrieveOwnerPetsAPIView(generics.RetrieveAPIView) :
    queryset = PetOwner.objects.all()
    serializer_class = OwnerPetsSerializer

class RetrievePetOwnerAPIView(generics.RetrieveAPIView) :
    queryset = Pet.objects.all()
    serializer_class = PetOwnerSerializer

class RetrievePetDatesAPIView(generics.RetrieveAPIView) :
    queryset = Pet.objects.all()
    serializer_class = PetDatesSerializer

"""# ViewSet

# class OwnersViewSet(viewsets.ModelViewSet) :
#      Viewset del modelo PetOwners

#     queryset = PetOwner.objects.all()
#     serializer_class = OwnersSerializer

# class PetsViewSet(viewsets.ModelViewSet) :
#      Viewset del modelo Pet 

#     queryset = Pet.objects.all().order_by('created_at')
#     serializer_class = PetsSerializer

# class PetDatesViewSet(viewsets.ModelViewSet) :
#      Viewset del modelo PetDate 

#     queryset = PetDate.objects.all()
#     serializer_class = PetDatesSerializer"""