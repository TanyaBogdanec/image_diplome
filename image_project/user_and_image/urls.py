from django.urls import path, include

from .views import *


urlpatterns = [
    path('image_upload/', image_view, name='image_upload'),
    path('success/', success, name='success'),
    path('home/', home, name='home'),
    path('user_image/<int:image_id>/', user_image, name='user_image'),
    path('upload/', image_upload_view, name='upload'),
    path('file_image/<int:user_id>/', file_img_view, name='file_image')
]

