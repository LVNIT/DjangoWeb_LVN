from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import *


def shoe_home(request):
    shoes = Shoe.objects.all()
    brands = Brand.objects.all()
    shoes_paginator = Paginator(shoes,3)
    page_number = request.GET.get('page')
    page_obj = shoes_paginator.get_page(page_number)
    context = {
        'shoes': page_obj,
        'brands': brands,

    }
    return render(request, 'store/home.html', context)


def shoe_search(request):
    if request.method == 'GET':
        query_search = request.GET.get('shoe_query')
        if query_search:
            shoes = Shoe.objects.filter(title__contains=query_search)
            return  render(request, 'store/home.html', {'shoes': shoes})
    return  redirect('store:home')


def brand_shoe(request, brand_slug):
    brand = get_object_or_404(Brand,slug=brand_slug)
    shoes = Shoe.objects.filter(brand_id=brand)
    return render(request, 'store/home.html', {'shoes': shoes})


def shoe_detail(request, shoe_slug):
    shoe = get_object_or_404(Shoe,slug=shoe_slug)
    return  render(request, 'store/shoes/detail.html', {'shoe': shoe})
