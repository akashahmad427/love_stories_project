from django import forms
from .models import Data
class Firstform(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('name','moral','story')
        #labels = {'name':'Name','moral':'Moral','story':'Story'}
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
                   'moral':forms.TextInput(attrs={'class':'form-control'}),
                   'story':forms.Textarea(attrs={'class':'form-control'})}
        