from rest_framework import serializers

from vet.models import PetOwner, Pet, PetDate

# Serializers define the API representation.
class OwnersSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = PetOwner
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'created_at',
        ]

class PetsSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Pet
        fields = [
            'id',
            'name',
            'type',
            'created_at',
        ]

class PetDatesSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = PetDate
        fields = [
            'id',
            'datetime',
            'type',
            'created_at',
        ]