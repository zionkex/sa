from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.cars_catalog, name='cars_catalog'),
    path('in-stock/', views.cars_in_stock, name='cars_in_stock'),

    path('<slug:slug>/', views.car_detail, name='car_detail'),
    path('brand/<slug:car_brand_slug>/', views.cars_by_brand, name='cars_by_brand'),

]
