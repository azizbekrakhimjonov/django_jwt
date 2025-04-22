from django.contrib import admin
from .models import CustomUser, Profile

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
   list_display = [field.name for field in CustomUser._meta.fields]


@admin.register(Profile)
class ProfilAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]
