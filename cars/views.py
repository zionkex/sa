from django.shortcuts import render
from .models import Car, CarBrand
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.db.models import F


def cars_catalog(request):
    transmission = Car.objects.order_by('transmission').values_list('transmission', flat=True).distinct()
    body_style = Car.objects.order_by('body_style').values_list('body_style', flat=True).distinct()
    wheel_drive = Car.objects.order_by('wheel_drive').values_list('wheel_drive', flat=True).distinct()
    fuel_type = Car.objects.order_by('fuel_type').values_list('fuel_type', flat=True).distinct()
    car_brand = CarBrand.objects.all().distinct()

    selected_transmission = request.GET.get('transmission', '')
    selected_body_style = request.GET.get('body_style', '')
    selected_car_brand = request.GET.get('car_brand', '')
    selected_wheel_drive = request.GET.get('wheel_drive', '')
    selected_fuel_type = request.GET.get('fuel_type', '')
    price_min = request.GET.get('price_min', '')
    price_max = request.GET.get('price_max', '')
    sort_price = request.GET.get('sort_price', '')

    car_list = Car.objects.filter(in_stock=False)

    if selected_car_brand:
        car_list = car_list.filter(car_brand_id=selected_car_brand)

    if selected_transmission:
        car_list = car_list.filter(transmission=selected_transmission)

    if selected_body_style:
        car_list = car_list.filter(body_style=selected_body_style)

    if selected_wheel_drive:
        car_list = car_list.filter(wheel_drive=selected_wheel_drive)

    if selected_fuel_type:
        car_list = car_list.filter(fuel_type=selected_fuel_type)

    if price_min:
        car_list = car_list.filter(price__gte=price_min)
    if price_max:
        car_list = car_list.filter(price__lte=price_max)

    if sort_price:
        if sort_price == 'asc':
            car_list = car_list.order_by('price')
        elif sort_price == 'desc':
            car_list = car_list.order_by('-price')

    paginator = Paginator(car_list, 6)
    page = request.GET.get('page')

    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)

    context = {
        'transmission': transmission,
        'body_style': body_style,
        'car_brand': car_brand,
        'wheel_drive': wheel_drive,
        'fuel_type': fuel_type,
        'selected_transmission': selected_transmission,
        'selected_body_style': selected_body_style,
        'selected_car_brand': selected_car_brand,
        'selected_wheel_drive': selected_wheel_drive,
        'selected_fuel_type': selected_fuel_type,
        'price_min': price_min,
        'price_max': price_max,
        'sort_price': sort_price,
        'car_list': cars,
    }

    return render(request, 'pages/catalog.html', context)


def cars_in_stock(request):
    transmission = Car.objects.order_by('transmission').values_list('transmission', flat=True).distinct()
    body_style = Car.objects.order_by('body_style').values_list('body_style', flat=True).distinct()
    wheel_drive = Car.objects.order_by('wheel_drive').values_list('wheel_drive', flat=True).distinct()
    fuel_type = Car.objects.order_by('fuel_type').values_list('fuel_type', flat=True).distinct()
    car_brand = CarBrand.objects.all().distinct()

    selected_transmission = request.GET.get('transmission', '')
    selected_body_style = request.GET.get('body_style', '')
    selected_car_brand = request.GET.get('car_brand', '')
    selected_wheel_drive = request.GET.get('wheel_drive', '')
    selected_fuel_type = request.GET.get('fuel_type', '')
    price_min = request.GET.get('price_min', '')
    price_max = request.GET.get('price_max', '')
    sort_price = request.GET.get('sort_price', '')

    car_list = Car.objects.filter(in_stock=True)

    if selected_car_brand:
        car_list = car_list.filter(car_brand_id=selected_car_brand)

    if selected_transmission:
        car_list = car_list.filter(transmission=selected_transmission)

    if selected_body_style:
        car_list = car_list.filter(body_style=selected_body_style)

    if selected_wheel_drive:
        car_list = car_list.filter(wheel_drive=selected_wheel_drive)

    if selected_fuel_type:
        car_list = car_list.filter(fuel_type=selected_fuel_type)

    if price_min:
        car_list = car_list.filter(price__gte=price_min)
    if price_max:
        car_list = car_list.filter(price__lte=price_max)

    if sort_price:
        if sort_price == 'asc':
            car_list = car_list.order_by('price')
        elif sort_price == 'desc':
            car_list = car_list.order_by('-price')

    paginator = Paginator(car_list, 6)
    page = request.GET.get('page')

    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)

    context = {
        'transmission': transmission,
        'body_style': body_style,
        'car_brand': car_brand,
        'wheel_drive': wheel_drive,
        'fuel_type': fuel_type,
        'selected_transmission': selected_transmission,
        'selected_body_style': selected_body_style,
        'selected_car_brand': selected_car_brand,
        'selected_wheel_drive': selected_wheel_drive,
        'selected_fuel_type': selected_fuel_type,
        'price_min': price_min,
        'price_max': price_max,
        'sort_price': sort_price,
        'car_list': cars,
    }

    return render(request, 'pages/catalog_in_stock.html', context)


def car_detail(request, slug):
    single_car = get_object_or_404(Car, slug=slug)

    similar_cars = Car.objects.filter(car_brand=single_car.car_brand).exclude(id=single_car.id)[:6]

    context = {
        'single_car': single_car,
        'similar_cars': similar_cars,
    }
    return render(request=request, template_name='pages/car_detail.html', context=context)


def cars_by_brand(request, car_brand_slug):
    transmission = Car.objects.order_by('transmission').values_list('transmission', flat=True).distinct()
    body_style = Car.objects.order_by('body_style').values_list('body_style', flat=True).distinct()
    car_brand = CarBrand.objects.all().distinct()

    brand = get_object_or_404(CarBrand, slug=car_brand_slug)

    car_list = Car.objects.filter(car_brand=brand)

    selected_transmission = request.GET.get('transmission', '')
    selected_body_style = request.GET.get('body_style', '')
    price_min = request.GET.get('price_min', '')
    price_max = request.GET.get('price_max', '')

    if selected_transmission:
        car_list = car_list.filter(transmission=selected_transmission)

    if selected_body_style:
        car_list = car_list.filter(body_style=selected_body_style)

    if price_min:
        car_list = car_list.filter(price__gte=price_min)
    if price_max:
        car_list = car_list.filter(price__lte=price_max)

    paginator = Paginator(car_list, 3)
    page = request.GET.get('page')

    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)

    context = {
        'brand': brand,
        'car_list': cars,
        'transmission': transmission,
        'body_style': body_style,
        'car_brand': car_brand,
        'selected_transmission': selected_transmission,
        'selected_body_style': selected_body_style,
        'price_min': price_min,
        'price_max': price_max,
    }
    return render(request, 'pages/cars_by_brand.html', context)
