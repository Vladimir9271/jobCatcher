from django.urls import path
from . import views

urlpatterns = [
    path('', views.vacancy_list, name='vacancy_list'),
    path('create/', views.vacancy_create, name='vacancy_create'),
    path('<slug:slug>/', views.vacancy_detail, name='vacancy_detail'),
]