from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.models import User

from .forms import ContactForm
from cars.models import Car, CarBrand


def index(request):
    cars_brand = CarBrand.objects.filter(is_featured=True).order_by('car_brand_name')[:6]

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']

            admin_info = User.objects.get(is_superuser=True)
            admin_email = admin_info.email
            send_mail(
                'Нове повідомлення з сайту',
                f'Ім\'я: {name}\nТелефон: +380{phone}',
                'vatikan98@gmail.com',
                [admin_email],
                fail_silently=False,
            )
            return redirect('pages:thank_you')

    else:
        form = ContactForm()

    context = {
        'form': form,
        'cars_brand': cars_brand,
    }

    return render(request, 'pages/index.html', context=context)


def draft(request):
    return render(request, 'pages/draft.html')


def contact(request):
    return render(request, 'pages/contact.html')


def thank_you(request):
    return render(request, 'pages/thank_you.html')
