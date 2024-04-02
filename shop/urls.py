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
                        create_category_view, update_product_view,
                        delete_product_view)

from user.views import register_view, login_view, profile_view, logout_view, confirm_sms_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_text),
    path('products/', shop_list_view),
    path('', main_page_view, name='main_page'),
    path('products/<int:product_id>/', products_detail_view),
    path('create_prod/', create_product_view),
    path('create_categ/', create_category_view),
    path('products/<int:product_id>/create_review/', create_review_view),
    path('products/<int:product_id>/update/', update_product_view),
    path('products/<int:product_id>/delete', delete_product_view),


    path('register/', register_view),
    path('login/', login_view),
    path('profile/', profile_view),
    path('logout/', logout_view),
    path('confirm_sms/', confirm_sms_view)
    #path('login/',)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
