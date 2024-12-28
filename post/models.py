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
    
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Catalog(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = 'Каталоги'
        verbose_name = 'Каталог'


class Product(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='products',
        null=True
    )
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
    
    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'



class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='reviews',
        null=True,
        
    )
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username if self.user else 'Anonymous'} on {self.product.name}"

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'


class OftenAskedQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name_plural = 'Часто задаваемые вопросы'
        verbose_name = 'Часто задаваемый вопрос'

