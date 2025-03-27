from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('packages/', views.packages, name='packages'),
    path('destination/', views.destination, name='destination'),
    path('reviews/', views.reviews, name='reviews'), 
    path('contact/', views.contact, name='contact'),
]
