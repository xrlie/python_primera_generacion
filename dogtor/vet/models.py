from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.contrib.gis.db import models
# from django.contrib.gis.geos import Point

# Create your models here.
class PetOwner(models.Model) :
  """ Pet Owner Model """
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  address = models.TextField(max_length=1000)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=20, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self) :
    return f'{self.first_name} {self.last_name}'

class Pet(models.Model) :
  """ Pet Model """
  name = models.CharField(max_length=255)

  PET_TYPES = (
    ('cat', 'Cat'),
    ('dog', 'Dog'),
    ('rabbit', 'Rabbit'),
    ('parrot', 'Parrot'),
  )
  type = models.CharField(max_length=50, choices=PET_TYPES, default='dog')
  created_at = models.DateTimeField(auto_now_add=True)

  # Relations
  owner = models.ForeignKey(PetOwner, on_delete=models.PROTECT, related_name='pets')

  def __str__(self) :
    return f'{self.name}, {self.type}'

class BranchOffice(models.Model) :
  """ Branch Office Model """
  alias = models.CharField(max_length=255)
  zip_code = models.CharField(max_length=12)
  address = models.TextField(max_length=1000)
  phone = models.CharField(max_length=20, unique=True)
  longitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
  latitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
  # location = models.PointField(geography=True, default=Point(0.0,0.0))
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self) :
    return f'{self.alias}'
  
  # def longitude(self) :
  #   return self.location.x

  # def latittude(self) :
  #   return self.location.y


class PetDate(models.Model) :
  """ Pets date Model """
  datetime = models.DateTimeField()

  DATE_TYPES = (
    ('esthetic', 'Esthetic'),
    ('disease', 'Disease'),
    ('vaccine', 'Vaccine'),
    ('deworming', 'Deworming'),
  )
  type = models.CharField(max_length=50, choices=DATE_TYPES, default='esthetic')
  created_at = models.DateTimeField(auto_now_add=True)

  # Relations
  pet = models.ForeignKey(Pet, on_delete=models.PROTECT, related_name='dates')
  office = models.ForeignKey(BranchOffice, null=True, on_delete=models.PROTECT, related_name='office_dates')

  def __str__(self) :
    return f'{self.datetime}, {self.pet.name}, {self.pet.type}'