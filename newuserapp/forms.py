from django import forms
from newuserapp.models import New_User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class LogInForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, initial="")
    

class SignUpForm(forms.ModelForm):
    
    class Meta:
        model = New_User
        fields = ['username', 'password','displayname', 'age', 'url']
