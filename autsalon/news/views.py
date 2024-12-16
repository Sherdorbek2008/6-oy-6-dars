from django.shortcuts import render, get_object_or_404
from .models import Brand, Car

def index(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    return render(request, 'news.html', {'brands': brands, 'cars': cars})

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)
    cars = brand.cars.all()
    return render(request, 'news.html', {'brand': brand, 'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'news.html', {'car': car})
