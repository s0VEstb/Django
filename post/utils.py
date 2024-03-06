from .models import Product

def create_100_products():
    products = []
    for i in range(100):
        prod = Product(
            name=f'Product {i}',
            price=100,
            content=f'Content {i}'
        )
        products.append(prod)

    Product.objects.bulk_create(products)