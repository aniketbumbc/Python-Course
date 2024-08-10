from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hello Aniket Welcome Django')


def newProduct(request):
    return HttpResponse("New Product pages")


def newStore(request):
    return HttpResponse("New Product store")
