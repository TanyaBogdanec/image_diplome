from django.views import View
from django.shortcuts import render, redirect
from rest_framework import generics

from .forms import UserCreationForm, ImageForm
from django.http import HttpResponse
from .models import Image
from django.contrib.auth import authenticate, login

from .serializer.image_serializer import ImageSerializer


class Register(View):
    """
    User registration
    Регистрация пользователя
    """
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


def image_upload_view(request):
    """
    Process images uploaded by users
    Обработка изображений, загруженных пользователями
    """
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'display_images', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'display_images.html', {'form': form})


def display_images(request):
    if request.method == 'GET':
        images = Image.objects.all()
        return render(request, 'display_images.html', {'images': images})


def upload_image_user_view(request):
    """
    Upload images and share them with other users.
    Загружать изображения и делиться ими с другими пользователями.
    """
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('user_image', image_id=image.pk)
    else:
        form = ImageForm()
    return render(request, 'user.html', {'form': form})


def user_image(request, image_id):
    image = Image.objects.get(pk=image_id)
    return render(request, 'user.html', {'image': image})


def image_view(request):
    """
    Accept a request from the user and return some HTML page.
    Принять запрос от пользователя и вернуть некоторую HTML - страницу.
    """
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'image.html', {'form': form})

def success(request):
    return HttpResponse(request, 'success.html')



class ImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

