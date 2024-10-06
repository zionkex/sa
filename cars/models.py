from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify


class CarBrand(models.Model):
    car_brand_name = models.CharField(max_length=50, verbose_name='Марка автомобіля')
    slug = models.SlugField(unique=True, verbose_name='Slug (Не редагувати)')
    car_brand_image = models.ImageField(upload_to='car_brand_images', verbose_name='Фото марки авто')
    is_featured = models.BooleanField(default=False, verbose_name='Показувати на головній сторінці')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['car_brand_name']
        verbose_name_plural = 'Марка Авто'

    def __str__(self):
        return self.car_brand_name

    def get_min_price(self):
        min_price_car = self.car_set.order_by('price').first()
        return min_price_car.price if min_price_car else None


class Car(models.Model):

    fuel_type_choices = (
        ('Дизель', 'Дизель'),
        ('Бензин', 'Бензин'),
        ('Гібрид', 'Гібрид'),
        ('Електро', 'Електро'),
    )

    wheel_drive_choices = (
        ('Повний', 'Повний'),
        ('Передній', 'Передній'),
        ('Задній', 'Задній'),
    )

    body_style_choices = (
        ('Седан', 'Седан'),
        ('Хетчбек', 'Хетчбек'),
        ('Універсал', 'Універсал'),
        ('Купе', 'Купе'),
        ('Кросовер', 'Кросовер'),
        ('Кабріолет', 'Кабріолет'),
        ('Родстер', 'Родстер'),
        ('Позашляховик', 'Позашляховик'),
        ('Мінівен', 'Мінівен'),
        ('Пікап', 'Пікап'),
        ('Мото', 'Мото'),
    )

    transmission_choices = (
        ('Автомат', 'Автомат'),
        ('Механіка', 'Механіка'),
    )

    car_title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, verbose_name='Марка авто')
    price = models.IntegerField(verbose_name='Ціна')
    car_title_photo = models.ImageField(upload_to='car_photos', verbose_name='Головне фото')
    car_photo_1 = models.ImageField(upload_to='car_photos', blank=True, null=True, verbose_name='Фото 2')
    car_photo_2 = models.ImageField(upload_to='car_photos', blank=True, null=True, verbose_name='Фото 3')
    car_photo_3 = models.ImageField(upload_to='car_photos', blank=True, null=True, verbose_name='Фото 4')
    car_photo_4 = models.ImageField(upload_to='car_photos', blank=True, null=True, verbose_name='Фото 5')
    car_photo_5 = models.ImageField(upload_to='car_photos', blank=True, null=True, verbose_name='Фото 6')
    car_photo_6 = models.ImageField(upload_to='car_photos', blank=True, null=True, verbose_name='Фото 7')
    car_photo_7 = models.ImageField(upload_to='car_photos', blank=True, null=True, verbose_name='Фото 8')
    car_photo_8 = models.ImageField(upload_to='car_photos', blank=True, null=True, verbose_name='Фото 9')

    mileage = models.IntegerField(verbose_name='Пробіг')
    year = models.IntegerField(verbose_name='Рік випуску')
    engine = models.CharField(max_length=100, verbose_name='Двигун', blank=True, null=True)
    fuel_type = models.CharField(max_length=50, verbose_name='Тип палива', choices=fuel_type_choices)
    transmission = models.CharField(max_length=100, verbose_name='Тип коробки передач', choices=transmission_choices)
    body_style = models.CharField(max_length=100, verbose_name='Тип кузова', choices=body_style_choices)
    wheel_drive = models.CharField(max_length=100, verbose_name='Привід', choices=wheel_drive_choices)
    color = models.CharField(max_length=100, verbose_name='Колір')
    interior_color = models.CharField(max_length=100, verbose_name='Колір салону')

    description = RichTextField(blank=True, null=True, verbose_name='Опис')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=False, verbose_name='Авто в наявності')

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = 'Всі Авто'

    def get_absolute_url(self):
        return reverse('catalog:car_detail', args=[self.slug])

    def __str__(self):
        return self.car_title
