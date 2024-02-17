'''
views - это Логика
'''
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from post.models import Product


# Create your views here
def hello_text(request):
    if request.method == 'GET':
        return render(request, 'hello_text.html')


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def current_data_text(request):
    return HttpResponse(datetime.now())


def shop_list_view(request):
    if request.method == 'GET':
        products = Product.objects.all()  # SELECT * FROM post
        return render(request,
                      'posts/product_list.html',
                      {'products': products}
                      )


def products_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
            return render(request,
                          'posts/product_detail.html',
                          {'product': product}
                          )
        except Product.DoesNotExist:
            return HttpResponse('404 Not Found')
