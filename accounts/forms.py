from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django import forms



class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label='Confirm Password')

    class Meta:
        model = User
        fields = (
            'username',
        )

class CustomUserAuthenticationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label='Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label='Password')

    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Invalid login or password. Try again.")