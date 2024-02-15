'''
models - это БазаДанных
'''

from django.db import models

#База Данных часов
class Post(models.Model):
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    name = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}: {self.price}"