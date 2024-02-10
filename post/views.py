'''
views - это Логика
'''
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here
def hello_text(request):
    return HttpResponse("Hello! it's my Project")

def current_data_text(request):
    return HttpResponse(datetime.now())

def goodbye_text(request):
    return HttpResponse("Goodbye user!")
