from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UsernameField
from allauth.account.forms import SignupForm


class CustomLoginForm(forms.Form):
    login = UsernameField(label="Email or Username")
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        login = cleaned_data.get("login")
        password = cleaned_data.get("password")

        user = authenticate(username=login, password=password)
        if user is None:
            raise forms.ValidationError("Invalid login credentials")
        self.user = user
        return cleaned_data

    def login_user(self, request):
        from django.contrib.auth import login
        login(request, self.user)

class CustomSignupForm(SignupForm):
    favourite = forms.CharField(max_length=100, label="What's your favourite thing?")

    def save(self, request):
        user = super().save(request)
        user.profile.favourite = self.cleaned_data['favourite']
        user.profile.save()
        return user
