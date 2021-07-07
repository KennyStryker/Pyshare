from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(*args, **kwargs):
    return HttpResponse("Hello World")