from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1 style = "color: red">This is a index page</h1>')

def detail(request):
    return HttpResponse('<h1 style = "color:blue">This is a detail page</h1>')
