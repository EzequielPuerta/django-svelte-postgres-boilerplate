from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from core.widgets.user_forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):  # type: ignore[type-arg]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
