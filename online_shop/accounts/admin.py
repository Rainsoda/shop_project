from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm
)

CustomUser = get_user_model()

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["id", "username", "email", "is_active", "is_staff", "is_superuser"]

    add_from = CustomUserCreationForm
    add_fieldsets = UserAdmin.add_fieldsets

    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets
