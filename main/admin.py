from django.contrib import admin
from .models import Job, Vacancy

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['job', 'name', 'slug', 'description', 'salary', 'available', 'created']
    list_filter = ['available', 'created', 'job']
    list_editable = ['salary', 'available']
    prepopulated_fields = {'slug': ('name',)}