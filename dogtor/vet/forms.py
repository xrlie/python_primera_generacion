from django import forms
from .models import PetOwner, Pet

# Create forms
class OwnerForm(forms.ModelForm) :
    class Meta :
        model = PetOwner
        fields = '__all__'
        widgets = {
            'email' : forms.EmailInput()
        }

class PetForm(forms.ModelForm) :
    class Meta :
        model = Pet
        fields = '__all__'
        widgets = {'email':forms.EmailInput()}
