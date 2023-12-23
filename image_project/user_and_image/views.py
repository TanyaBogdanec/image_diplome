from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, ImageForm
from django.http import HttpResponse
from .models import Image
from django.shortcuts import get_object_or_404




def file_img_view(request, user_id):
    """
    Process images uploaded by users
    Обработка изображений загруженных пользователями
    """
    file_image = get_object_or_404(Image, pk=user_id)
    context = {'file_image': file_image}
    return render(request, 'index.html', context)


def image_upload_view(request):
    """
    Process images uploaded by users
    Обработка изображений, загруженных пользователями
    """
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'image.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'image.html', {'form': form})


def signup_view(request):
    """
    User registration
    Регистрация пользователя
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        User.objects.create_user(username=username, password=password)

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})

def home(request):
    return HttpResponse(request, 'home.html')


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



