from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('email', 'first_name', 'last_name',
                    'is_superuser', 'is_staff', 'is_active', 'created')

    list_filter = ('is_superuser', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email',
                           'password', 'gender', 'birthday')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email',
                       'password1', 'password2', 'gender',
                       'birthday', 'is_staff', 'is_active')}
         ),
    )

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
