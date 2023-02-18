from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('frontpage/', views.frontpage, name='frontpage'),
]