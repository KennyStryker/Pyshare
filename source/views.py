from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request, *args, **kwargs):
    return render(request, "login.html")