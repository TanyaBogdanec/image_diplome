from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['file_img', 'description', 'category', 'user', 'delete', 'uploaded_at', 'updated_at', 'deleted_at']


User = get_user_model()
class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
