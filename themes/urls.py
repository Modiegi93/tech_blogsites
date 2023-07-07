#!/usr/bin/python3
from django.urls import path
from . import views

app_name = 'themes'

urlpatterns = [
        path('', views.theme_list, name='theme_list'),
        path('<int:theme_id>/', views.theme_detail, name='theme_detail'),
]
