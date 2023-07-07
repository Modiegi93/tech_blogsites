#!/usr/bin/python3

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
        path('create/', views.create_blog_post, name='create'),
        path('<int:pk>/', views.blog_post_detail, name='detail'),
        path('', views.blog_post_list, name='list'),
        path('drafts/', views.drafts_list, name='drafts'), #
