from django import forms
from blog.models import Blog
from django.contrib.auth.models import User

class RegisterForms(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password','email')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Username'
                }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Email'
                }),
                 'password': forms.PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Password'
                 })
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields ='__all__'
        exclude=['is_published']

class Login_form(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password')  
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Username'
                }),
                 'password': forms.PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Password'
                 })
        }
