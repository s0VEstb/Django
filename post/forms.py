from django import forms
from post.models import Product, Review, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'content', 'price', 'category', 'catalog']
        labels = {'image': 'Картинка',
                  'name': 'Название',
                  'content': 'Содержание',
                  'price': 'Цена',
                  'category': 'Категория',
                  'catalog': 'Каталог'}

    def clean_name(self):
        name = self.cleaned_data['name']
        if 'Kanat' in name.capitalize():
            raise forms.ValidationError('Invalid name')
        return name

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data['name']
        content = cleaned_data['content']
        if name == content:
            raise forms.ValidationError('Invalid')
        return cleaned_data


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        labels = {'text': 'Отзыв'}


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        labels = {'name': 'Название',
                  'description': 'Описание'}

