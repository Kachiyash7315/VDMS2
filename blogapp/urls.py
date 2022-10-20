from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('', views.blogpage,name='blogPage'),
path('<str:slug>', views.blogPost,name='blogPost'),


]