from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_create/', view.admin_create, name="admin_create"), 
    path('admin_event/', view.admin_event, name="admin_event"),
]
