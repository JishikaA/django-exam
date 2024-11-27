from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput

from new_app.models import Login, Customer, Seller, Blog


class LoginForm(UserCreationForm):
    username =forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput)

    class Meta:
        model =Login
        fields =("username","password1","password2",)

class CustomerForm(forms.ModelForm):
    class Meta:
        model =Customer
        fields ="__all__"
        exclude =("user",)

class SellerForm(forms.ModelForm):
    class Meta:
        model =Seller
        fields ="__all__"
        exclude =('user',)

class BlogForm(forms.ModelForm):
    class Meta:
        model =Blog
        fields ="__all__"
        exclude =("user",)