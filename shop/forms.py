from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError
import re


class CustomLoginForm(forms.Form):
    login = UsernameField(
        label="Email or Username",
        widget=forms.TextInput(attrs={"placeholder": "Email or Username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

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
    favourite = forms.CharField(
        max_length=100,
        # can change this to a more specific question
        label="What's your favourite thing?", 
        # can change this to a more specific placeholder
        widget=forms.TextInput(attrs={"placeholder": "Pizza, Python, etc."})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update({"placeholder": "Email address"})
        self.fields["username"].widget.attrs.update({"placeholder": "Username"})
        self.fields["password1"].widget.attrs.update({"placeholder": "Password"})
        self.fields["password2"].widget.attrs.update({"placeholder": "Password (again)"})

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError("That username is taken.")
        return username

    def clean_password1(self):
        password = self.cleaned_data.get("password1")

        # Enforce password strength
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r"\d", password):
            raise ValidationError("Password must contain at least one number.")
        if not re.search(r"[A-Z]", password):
            raise ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValidationError("Password must contain at least one special character.")

        return password

    def save(self, request):
        user = super().save(request)
        user.profile.favourite = self.cleaned_data["favourite"]
        user.profile.save()
        return user
