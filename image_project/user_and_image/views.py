from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ImageForm
from django.http import HttpResponse
from .models import Image



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
            return render(request, 'image.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'display_images', {'form': form})


def display_images(request):
    if request.method == 'GET':
        images = Image.objects.all()
        return render(request, 'display_images.html', {'images': images})


def register_view(request):
    """
    User registration
    Регистрация пользователя
    """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


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



