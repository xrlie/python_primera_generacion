from django.urls import path

from .views import Owners, OwnersList, OwnerDetail    # list_pet_owners, Test
from .views import Pets, PetDetail

urlpatterns = [
    path('owners/', OwnersList.as_view()), # list_pet_owners),
    path('owners/<int:pk>', OwnerDetail.as_view()),
    path('pets/', Pets.as_view()),
    path('pets/<int:pk>', PetDetail.as_view()),
    # path('test/', Test.as_view()),
]