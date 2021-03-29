from django.shortcuts import render

from rest_framework import generics # viewsets

from vet.models import PetOwner, Pet, PetDate, BranchOffice

# Relations serializers
from .serializers import (
  # Views serializers
  BranchOfficesListSerializer,
  BranchOfficesSerializer,
  OwnersListSerializer,
  OwnersSerializer,
  PetsListSerializer,
  PetsSerializer,
  DatesListSerializer,
  DatesSerializer,
  #Relations
  OwnerPetsSerializer,
  PetOwnerSerializer,
  PetDatesSerializer,
  BranchOfficeDatesSerializer,
  OwnerPetsDatesSerializer,
)
# from .serializers import OwnersSerializer, PetsSerializer
# from .serializers import PetDatesSerializer

# # Create your views here.

# Generic Views
# BranchOffices Views
class ListBranchOfficesAPIView(generics.ListAPIView) :
  queryset = BranchOffice.objects.all()
  serializer_class = BranchOfficesListSerializer

class CreateBranchOfficesAPIView(generics.CreateAPIView) :
  queryset = BranchOffice.objects.all()
  serializer_class = BranchOfficesSerializer

class RetrieveBranchOfficesAPIView(generics.RetrieveAPIView) :
  queryset = BranchOffice.objects.all()
  serializer_class = BranchOfficesSerializer

class UpdateBranchOfficesAPIView(generics.UpdateAPIView) :
  queryset = BranchOffice.objects.all()
  serializer_class = BranchOfficesSerializer

class DestroyBranchOfficesAPIView(generics.DestroyAPIView) :
  queryset = BranchOffice.objects.all()
  serializer_class = BranchOfficesSerializer

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

## Dates Views
class ListDatesAPIView(generics.ListAPIView) :
  queryset = PetDate.objects.all()
  serializer_class = DatesListSerializer

class CreateDatesAPIView(generics.CreateAPIView) :
  queryset = PetDate.objects.all()
  serializer_class = DatesSerializer

class RetrieveDatesAPIView(generics.RetrieveAPIView) :
  queryset = PetDate.objects.all()
  serializer_class = DatesSerializer

class UpdateDatesAPIView(generics.UpdateAPIView) :
  queryset = PetDate.objects.all()
  serializer_class = DatesSerializer

class DestroyDatesAPIView(generics.DestroyAPIView) :
  queryset = PetDate.objects.all()
  serializer_class = DatesSerializer

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

class RetrieveBranchOfficesDatesAPIView(generics.RetrieveAPIView) :
  queryset = BranchOffice.objects.all()
  serializer_class = BranchOfficeDatesSerializer

class RetrieveOwnerPetsDatesAPIView(generics.RetrieveAPIView) :
  queryset = PetOwner.objects.all()
  serializer_class = OwnerPetsDatesSerializer







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