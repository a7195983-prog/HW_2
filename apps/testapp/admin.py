from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    
    list_display = ('email', 'role', 'is_verified', 'is_active')
    
    list_filter = ('role', 'is_verified', 'is_staff', 'is_superuser', 'is_active')
    
    search_fields = ('email', 'username')
    
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'username', 'bio', 'birth_date')}),
        (_('Permissions'), {'fields': ('role', 'is_verified', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Настройка формы создания нового пользователя через админку
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'role', 'is_verified', 'bio', 'birth_date'),
        }),
    ) 