from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    email = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control',})
    )
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={'class': 'form-control',})
    )

    class Meta:
        model = User
        fields = ['email', 'password']