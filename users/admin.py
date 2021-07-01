from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from .forms import UserCreateFormAdmin, UserChangeFormAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


# get user model
User = get_user_model()

class UserAdmin(BaseAdmin):
    add_form = UserCreateFormAdmin
    form = UserChangeFormAdmin
    list_display = ["email", "username", "birth_date", "bio", "age", "user_level"]
    list_filter = ["is_admin", "is_active", "user_level"]
    fieldsets = [
        (None, {"fields":["email", "username"]}),
        ("اطلاعات شخصی", {"fields":["age", "birth_date", "bio", "wallet_stock", "password", "experiments", "user_level"]}),
        ("دسترسی ها", {"fields":["is_admin", "is_active", "user_type"]})
    ]
    add_fieldsets = [
        (None, {"fields":["email","username","birth_date",
        "age", "password", "repeated_password", "user_type"]})
    ]
    
    search_fields = ["email", "username", "user_type"]
    ordering = ["-is_admin", "email"]
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group) 