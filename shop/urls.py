"""
urls.py - файл маршрутизации проекта
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from post.views import (hello_text, shop_list_view,
                        main_page_view, products_detail_view,
                        create_product_view, create_review_view,
                        create_category_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_text),
    path('products/', shop_list_view),
    path('', main_page_view),
    path('products/<int:product_id>/', products_detail_view),
    path('create_prod/', create_product_view),
    path('create_categ/', create_category_view),
    path('products/<int:product_id>/create_review/', create_review_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
