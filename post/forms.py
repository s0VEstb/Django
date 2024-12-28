from django import forms
from post.models import Product, Review, Category, OftenAskedQuestion

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'content', 'price', 'image', 'category', 'catalog']

    def clean_name(self):
        name = self.cleaned_data['name']
        if 'Kanat' in name.capitalize():
            raise forms.ValidationError('Invalid name Kanat')
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


class OAF(forms.ModelForm):
    class Meta:
        model = OftenAskedQuestion
        fields = ['question', 'answer']
        labels = {'question': 'Вопрос',
                  'answer': 'Ответ'}

