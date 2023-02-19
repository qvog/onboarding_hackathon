from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('', views.topic, name='topic'),
    path('topic_page/', views.topic_page, name='topic_page'),
]