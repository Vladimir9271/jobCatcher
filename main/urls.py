from django.urls import path
from . import views

urlpatterns = [
    path('vacancies/', views.vacancy_list, name='vacancy_list'),
    path('vacancies/<slug:slug>/', views.vacancy_detail, name='vacancy_detail'),
]