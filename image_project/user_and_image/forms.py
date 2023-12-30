from django import forms
from .models import *


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['file_img', 'description', 'category', 'user', 'delete', 'uploaded_at', 'updated_at', 'deleted_at']


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput())

    class Meta:
        model = Image
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']