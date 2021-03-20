from django import forms
from .models import PetOwner

# Create forms
class OwnerForm(forms.ModelForm) :
    class Meta :
        model = PetOwner
        fields = '__all__'
        widgets = {
            'email' : forms.EmailInput()
        }
