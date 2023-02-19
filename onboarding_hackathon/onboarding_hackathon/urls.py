from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('core.urls')),
    path('courses/', include('courses.urls')),
    path('topic/', include('forum.urls')),
    path('admin/', admin.site.urls),
]
