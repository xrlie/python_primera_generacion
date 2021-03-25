from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View   # gives behavior for class Test
# from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .models import PetOwner, Pet, PetDate
from .forms import OwnerForm, PetForm, PetDateForm

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

class OwnersList(LoginRequiredMixin, ListView) :
    model = PetOwner
    template_name = 'vet/owners/list.html'
    context_object_name = 'owners'
    login_url = reverse_lazy('login')

class OwnerDetail(LoginRequiredMixin, DetailView) :
    model = PetOwner
    template_name = 'vet/owners/detail.html'
    context_object_name = 'owner'
    login_url = reverse_lazy('login')

class OwnersCreate(LoginRequiredMixin, CreateView) :
    model = PetOwner
    template_name = 'vet/owners/create.html'
    form_class = OwnerForm
    success_url = reverse_lazy('vet:owners_list')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['owners'] = PetOwner.objects.all().order_by('created_at')
        print(context)
        return context

class OwnersUpdate(LoginRequiredMixin, UpdateView) :
    model = PetOwner
    form_class = OwnerForm
    template_name = 'vet/owners/update.html'
    success_url = reverse_lazy('vet:owners_list')
    login_url = reverse_lazy('login')

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

class Pets(LoginRequiredMixin, ListView) :
    model = Pet
    template_name = 'vet/pets/list.html'
    context_object_name = 'pets'
    login_url = reverse_lazy('login')

class PetDetail(LoginRequiredMixin, DetailView) :
    model = Pet
    template_name = 'vet/pets/detail.html'
    context_object_name = 'pet'
    login_url = reverse_lazy('login')

    def get_initial(self) :
        initial = {}
        for queryparam in self.request.GET :
            initial[queryparam] = self.request.GET[queryparam]
        return initial

class PetsCreate(LoginRequiredMixin, CreateView) :
    model = Pet
    template_name = 'vet/pets/create.html'
    # form_class = PetForm
    fields = ['name', 'type', 'owner']
    success_url = reverse_lazy('vet:pets_list')
    login_url = reverse_lazy('login')

    def get_initial(self) :
        initial = {}
        for queryparam in self.request.GET :
            initial[queryparam] = self.request.GET[queryparam]
            # print(queryparam, self.request.GET)
        return initial

class PetsUpdate(LoginRequiredMixin, UpdateView) :
    model = Pet
    form_class = PetForm
    template_name = 'vet/pets/update.html'
    success_url = reverse_lazy('vet:owners_list')
    login_url = reverse_lazy('login')

class PetDateCreate (LoginRequiredMixin, CreateView) :
    model = PetDate
    template_name = 'vet/dates/create.html'
    form_class = PetDateForm
    # success_url = reverse_lazy('vet:pet_detail')
    login_url = reverse_lazy('login')

    def get_success_url(self) :
        success_url = reverse_lazy('vet:pet_detail',args=(self.object.pet_id,))
        # print(self.object.__dict__)
        return success_url

    def get_initial(self) :
        initial = {}
        for queryparam in self.request.GET :
            initial[queryparam] = self.request.GET[queryparam]
        return initial