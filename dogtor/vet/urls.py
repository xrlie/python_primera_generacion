from django.urls import path

from .views import OwnersCreate, OwnersUpdate, OwnersList, OwnerDetail    # list_pet_owners, Test
from .views import PetsCreate, PetsUpdate, Pets, PetDetail

urlpatterns = [
    # Reverse URL's incluimos name=
    path('owners/', OwnersList.as_view(), name='owners_list'), # list_pet_owners),
    path('owners/<int:pk>/', OwnerDetail.as_view(), name='owner_detail'),
    path('owners/add/', OwnersCreate.as_view(), name='owner_create'),
    path('owners/<int:pk>/update/', OwnersUpdate.as_view(), name='owner_update'),
    path('pets/', Pets.as_view(), name='pets_list'),
    path('pets/<int:pk>/', PetDetail.as_view(), name='pet_detail'),
    path('pets/add/', PetsCreate.as_view(), name='pet_create'),
    path('pets/<int:pk>/update/', PetsUpdate.as_view(), name='pet_update'),
    # path('test/', Test.as_view()),
]