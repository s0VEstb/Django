'''
models - это БазаДанных
'''

from django.db import models

#База Данных часов
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Catalog(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    name = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.CASCADE,
        related_name='category'
    )
    catalog = models.ForeignKey(
        Catalog,
        null=True,
        on_delete=models.CASCADE,
        related_name='catalog'
    )


    def __str__(self):
        return f"{self.category}. {self.name}: {self.price}"


class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment for {self.product.name}"

