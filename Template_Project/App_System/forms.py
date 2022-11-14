from django import forms 
from django.forms import ModelForm
from .models import Equipment 

#Create a equipment form 
class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        #fields = "__all__" #If we wanna all the fields. 
        fields = ('tag', 'address', 'type')

        labels = {
            'tag': '' ,
            'address': '' ,
            'type': '' ,           
        }

        widgets = {
            'tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tag'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Equipment Type'}),          
        }
