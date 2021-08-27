from django import forms
from django.contrib.auth.models import User
from .models import UserInfo

class UserForm(forms.ModelForm):

    password = forms.CharField(label="Password",widget=forms.PasswordInput())

    class Meta():

        model = User
        fields = ("username","email","password",)

class UserInfoForm(forms.ModelForm):

    class Meta():

        model = UserInfo
        exclude = ("user",)

class LogInForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())