from django.urls import path, include

from .views import *
from .views import Register

from .views import ImageListCreateAPIView, ImageDetailAPIView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('image_upload/', image_view, name='image_upload'),
    path('success/', success, name='success'),
    path('user_image/<int:image_id>/', user_image, name='user_image'),
    path('upload/', image_upload_view, name='upload'),
    path('display_images/', display_images, name='display_images'),
    path('images/', ImageListCreateAPIView.as_view(), name='image-list-create'),
    path('images//', ImageDetailAPIView.as_view(), name='image-detail'),
]

