from django.shortcuts import render
from django.http import HttpResponse

def any(request):
    return HttpResponse("<h1>i am porkodi</h1>")

# Create your views here.
