from django.urls import path, include

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('draft/', views.draft, name='draft'),
]
