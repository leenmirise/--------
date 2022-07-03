from django import forms
from .models import User

class userForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

class UserForm(forms.Form):
    username = forms.CharField(label = "Login:", required = True)
    userpass = forms.CharField(label = "Password:", widget=forms.PasswordInput, required = True)

class RegUser(forms.ModelForm):
    class Meta:
        model = User
        fields='__all__'

        # username = forms.CharField(label = "Login:", required = True)
        # userpass = forms.CharField(label = "Password:", widget=forms.PasswordInput, required = True)
        # userrole = forms.ChoiceField(required = True, choices = roles)