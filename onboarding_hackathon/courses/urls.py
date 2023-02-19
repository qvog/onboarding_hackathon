from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
]