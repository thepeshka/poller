from django import forms
from django.contrib.auth import authenticate
from django.forms import CharField, PasswordInput

from authentication.models import User


class LoginForm(forms.Form):
    username = CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self):
        cleaned_data = self.cleaned_data
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))

        if user is not None and not user.is_anonymous:
            setattr(self, 'user', user)
            return cleaned_data
        else:
            raise forms.ValidationError(
                "Unknown user"
            )


class RegistrationForm(forms.Form):
    username = CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self):
        cleaned_data = self.cleaned_data
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = User.objects.filter(username=self.cleaned_data.get('username')).first()

        if user:
            raise forms.ValidationError(
                "User with this username already created!"
            )
        else:
            setattr(self, 'username', username)
            setattr(self, 'password', password)
            return cleaned_data

