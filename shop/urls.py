"""
urls.py - файл маршрутизации проекта
"""
from django.contrib import admin
from django.urls import path
from post.views import (hello_text, current_data_text,
                        goodbye_text, shop_list_view,
                        main_page_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_text),
    path('current_data/', current_data_text),
    path('goodbye/', goodbye_text),
    path('products/', shop_list_view),
    path('', main_page_view)
]
