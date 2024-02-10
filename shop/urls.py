"""
urls.py - файл маршрутизации проекта
"""
from django.contrib import admin
from django.urls import path
from post.views import hello_text, current_data_text, goodbye_text

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_text),
    path('current_data/', current_data_text),
    path('goodbye/', goodbye_text)
]
