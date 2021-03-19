from django.urls import path

from .views import Owners, OwnersList, OwnerDetail    # list_pet_owners, Test
from .views import Pets, PetDetail

urlpatterns = [
    # Reverse URL's incluimos name=
    path('owners/', OwnersList.as_view(), name='owners_list'), # list_pet_owners),
    path('owners/<int:pk>', OwnerDetail.as_view(), name='owner_detail'),
    path('pets/', Pets.as_view(), name='pets_list'),
    path('pets/<int:pk>', PetDetail.as_view(), name='pet_detail'),
    # path('test/', Test.as_view()),
]