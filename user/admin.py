from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile_image
from .forms import SignUpForm, CustomUserChangeForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = CustomUserChangeForm
    model = User
    list_display=["email", "username", ]

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile_image)