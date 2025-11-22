from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    date_of_birth = forms.DateField(required=False, label="Дата народження", widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    avatar = forms.ImageField(required=False, label="Аватар")
    bio = forms.CharField(required=False, label="Про себе", widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}))
    phone = forms.CharField(required=False, label="Номер телефону", widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2",
                  "date_of_birth", "avatar", "bio", "phone", "role")

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Логін", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label=forms.PasswordInput(attrs={"class": "form-control"}))

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email", "date_of_birth", "avatar", "bio", "phone")
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "date_of_birth": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "bio": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "phone": forms.TextInput(attrs={"class": "form-control"})
        }