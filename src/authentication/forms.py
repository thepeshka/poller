from django import forms
from django.contrib.auth import authenticate
from django.forms import CharField, PasswordInput


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
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))

        if user is not None and not user.is_anonymous:
            setattr(self, 'user', user)
            return cleaned_data
        else:
            raise forms.ValidationError(
                "Unknown user"
            )

