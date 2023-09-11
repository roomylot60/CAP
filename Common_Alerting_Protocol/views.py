from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def header(request):
    return render(request, 'header.html')

def create(request):
    return

def message(request):
    return

def area(request):
    return
