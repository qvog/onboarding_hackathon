from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.frontpage, name='frontpage'),

    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
]