from django.shortcuts import render
from .models import *


def index_page(request):
    return render(request, 'product/index.html')
    

def men_page(request):
    return render(request, 'product/men.html')


def women_page(request):
    return render(request, 'product/women.html')


def get_jacket(request, slug):
    jackets = Jacket.objects.filter(slug__iexact=slug)
    return render(request, 'product/jackets.html', {'jackets':jackets})

def get_shirt(request, slug):
    shirts = Shirt.objects.filter(slug__iexact=slug)
    return render(request, 'product/shirts.html', {'shirts':shirts})

def get_pants(request, slug):
    pants = Pants.objects.filter(slug__iexact=slug)
    return render(request, 'product/pants.html', {'pants':pants})

def get_footwear(request, slug):
    footwears = Footwear.objects.filter(slug__iexact=slug)
    return render(request, 'product/footwears.html', {'footwears':footwears})

def get_accessories(request, slug):
    accessories = Accessory.objects.filter(slug__iexact=slug)
    return render(request, 'product/accessories.html', {'accessories':accessories})