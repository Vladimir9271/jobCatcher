from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Показывать в списке
    list_display = ('username', 'email', 'role', 'is_staff', 'date_joined')
    
    # Фильтровать по роли
    list_filter = ('role', 'is_staff', 'is_superuser')
    
    # Добавляем поле role при редактировании
    fieldsets = UserAdmin.fieldsets + (
        ('Роль', {'fields': ('role',)}),
    )
    
    # Добавляем поле role при создании
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Роль', {'fields': ('role',)}),
    )