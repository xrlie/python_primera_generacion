from django import forms
from .models import PetOwner, Pet, PetDate

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

class PetDateForm(forms.ModelForm) :
    class Meta :
        model = PetDate
        fields = '__all__'
        # widgets = {'datetime':forms.DateTimeField()}
        widgets = {'datetime':forms.SelectDateWidget(
            empty_label=('Choose Year', 'Choose Month', 'Choose Day')
        )}