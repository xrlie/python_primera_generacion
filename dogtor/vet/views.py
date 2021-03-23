from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View   # gives behavior for class Test
# from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .models import PetOwner, Pet
from .forms import OwnerForm, PetForm

# Create your views here.
def list_pet_owners(request) :
    """ List owners """
    owners = PetOwner.objects.all()
    context = {'owners': owners}

    template = loader.get_template('vet/owners/list.html')
    return HttpResponse(template.render(context, request))

# def test(request) :
#     return HttpResponse('Hello world!!')

# class Test(View) :
#     def get(self, request) :
#         return HttpResponse('Hello world from class view!!!')

class Owners(View) :
    def get(self, request) :
        owners = PetOwner.objects.all()
        context = {'owners': owners}

        template = loader.get_template('vet/owners/list.html')
        return HttpResponse(template.render(context, request))

# class OwnersList(TemplateView) :
#     template_name = 'vet/owners/list.html'

#     def get_context_data(self, **kwargs) :
#         context = super().get_context_data(**kwargs)
#         context['owners'] = PetOwner.objects.all()
#         return context

class OwnersList(ListView) :
    model = PetOwner
    template_name = 'vet/owners/list.html'
    context_object_name = 'owners'

class OwnerDetail(DetailView) :
    model = PetOwner
    template_name = 'vet/owners/detail.html'
    context_object_name = 'owner'

class OwnersCreate(CreateView) :
    model = PetOwner
    template_name = 'vet/owners/create.html'
    form_class = OwnerForm
    success_url = reverse_lazy('vet:owners_list')

# class Pets(View) :
#     def get(self, request) :
#         pets = Pet.objects.all()
#         context = {'pets': pets}

#         template = loader.get_template('vet/pets/list.html')
#         return HttpResponse(template.render(context, request))

# class PetDetail(View) :
#     def get(self, request, pk) :
#         pet = Pet.objects.get(id=pk)
#         context = {'pet': pet}
        
#         template = loader.get_template('vet/pets/detail.html')
#         return HttpResponse(template.render(context, request))

class Pets(ListView) :
    model = Pet
    template_name = 'vet/pets/list.html'
    context_object_name = 'pets'

class PetDetail(DetailView) :
    model = Pet
    template_name = 'vet/pets/detail.html'
    context_object_name = 'pet'

class PetsCreate(CreateView) :
    model = Pet
    template_name = 'vet/pets/create.html'
    # form_class = PetForm
    fields = ['name', 'type', 'owner']
    success_url = reverse_lazy('vet:pets_list')