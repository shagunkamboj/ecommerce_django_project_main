from django import forms
from .models import * 
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, ImageField
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields ='__all__'


class RegisterForms(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class login_product(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password') 
class AddressForm(forms.ModelForm):
       class Meta:
        model = AddressModel
        fields = ('address','city','zip_code')
        widgets = {
            'address': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Address'
                }),
                'city': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'State'
                }),
                'zip_code': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'zip_code'
                }),
                
               
         }
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'address', 'phone']