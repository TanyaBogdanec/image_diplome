from django.contrib import admin
from .models import Category, Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ("category", "user", "updated_at", "uploaded_at")
    list_filter = ("category", "uploaded_at", "updated_at")
    search_fields = ("uploaded_at", "description", "updated_at")


admin.site.register(Category)
admin.site.register(Image, ImageAdmin)



