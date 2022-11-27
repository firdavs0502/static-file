from django.shortcuts import render
from .models import Mashina
# Create your views here.


def index1(request):
    return render(request, 'about.html')

def index2(request):
    return render(request, 'contact.html')

def index3(request):
    return render(request, 'furnitures.html')

def index4(request):
    return render(request, 'index.html')

def index5(request):
    return render(request, 'testimonial.html')