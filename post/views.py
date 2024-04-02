'''
views - это Логика
'''
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Q
from post.forms import ProductForm, ReviewForm, CategoryForm
from post.models import Product, Review, Catalog, Category
from django.contrib.auth.decorators import login_required


# Create your views here
def hello_text(request):
    if request.method == 'GET':
        return render(request, 'hello_text.html')


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def shop_list_view(request):
    if request.method == 'GET':

        search = request.GET.get("search")
        category_id = request.GET.get("category")
        sort = request.GET.get("sort")
        page = request.GET.get("page", 1)

        category = Category.objects.all()
        products = Product.objects.all()  # SELECT * FROM post

        limit = 6
        max_pages = len(products) / limit
        if max_pages != 0:
            max_pages = int(max_pages) + 1
        pages = [i for i in range(1, max_pages + 1)]

        start = (int(page) - 1) * limit
        end = start + limit

        if sort == "price<":
            products = products.order_by("price")

        if sort == "price>":
            products = products.order_by("-price")

        if sort == "newest":
            products = products.order_by("-created_at")
            print(products)

        if sort == "oldest":
            products = products.order_by("created_at")


        if search:
            products = products.filter(
                Q(name__icontains=search) |
                Q(content__icontains=search) |
                Q(category__name__icontains=search) |
                Q(catalog__name__icontains=search)
            )
        if category_id:
            products = products.filter(
                category=category_id
            )

        products = products[start:end]



        return render(request,
                      'products/product_list.html',
                      {'products': products,
                       'category': category,
                       "pages": pages}
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
        product = form.save()
        product.user = request.user
        product.save()
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


@login_required(login_url='/login/')
def update_product_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        form = ProductForm(instance=product)
        return render(request,
                      'products/update_product.html',
                      context={"form": form})
    elif request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if not form.is_valid():
            return render(request,
                          'products/update_product.html',
                          context={'form': form})
        form.save()
        return redirect('/products/')


@login_required(login_url='/login/')
def delete_product_view(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('/products/')
