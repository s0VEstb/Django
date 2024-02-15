'''
views - это Логика
'''
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from post.models import Post

# Create your views here
def hello_text(request):
    if request.method == 'GET':
        return render(request, 'hello_text.html')


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def current_data_text(request):
    return HttpResponse(datetime.now())

def goodbye_text(request):
    return HttpResponse("Goodbye user!")

def shop_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all() #SELECT * FROM post

        return render(request,
                      'posts/post_list.html',
                      {'posts': posts}
                      )
