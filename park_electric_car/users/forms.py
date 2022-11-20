from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ""
        self.fields['email'].help_text = ""
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class VINForm(forms.Form):
    vin = forms.CharField(max_length=30)
