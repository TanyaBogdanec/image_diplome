from django import forms
from .models import *


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['file_img', 'description', 'category', 'user', 'delete', 'uploaded_at', 'updated_at', 'deleted_at']


class SignUpForm(forms.Form):
    email = forms.EmailField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Image