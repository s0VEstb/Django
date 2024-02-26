'''
views - это Логика
'''
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

from post.forms import ProductForm, ReviewForm, CategoryForm
from post.models import Product, Review, Catalog


# Create your views here
def hello_text(request):
    if request.method == 'GET':
        return render(request, 'hello_text.html')


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def shop_list_view(request):
    if request.method == 'GET':
        products = Product.objects.all()  # SELECT * FROM post
        return render(request,
                      'products/product_list.html',
                      {'products': products}
                      )


def products_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return HttpResponse('404 Not Found')
        form = ReviewForm()
        context = {'product': product, 'form': form}

        return render(request,
                      'products/product_detail.html',
                      context=context)

def create_review_view(request, product_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if not form.is_valid():
            return render(request,
                      'products/product_detail.html',
                      context={'form': form})
        review = form.save(commit=False)
        review.product_id = product_id
        review.save()

        return redirect(f'/products/{product_id}')

def create_product_view(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request,
                      'products/create_product.html',
                      context={"form": form})
    elif request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request,
                          'products/create_product.html',
                          context={"form": form})
        form.save()
        return redirect('/products/')
    # Product.objects.create(
    #     image=form.cleaned_data['image'],
    #     name=form.cleaned_data['name'],
    #     content=form.cleaned_data['content'],
    #     price=form.cleaned_data['price'],
    #     category=form.cleaned_data['category'],
    #     catalog=form.cleaned_data['catalog']
    # )
    # Product.objects.create(**form.cleaned_data)

def create_category_view(request):
    if request.method == "GET":
        form = CategoryForm()
        return render(request,
                      'products/create_category.html',
                      context={"form": form})
    elif request.method == "POST":
        form = CategoryForm(request.POST)
        if not form.is_valid():
            return render(request,
                          'products/create_category.html',
                          context={"form": form})
        form.save()
        return redirect('/products/')





