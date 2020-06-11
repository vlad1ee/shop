from django.contrib import admin
from django.urls import path, include 
from .views import *

urlpatterns = [
    path('', index_page, name='index_page_url'),
    path('men/', men_page, name='men_url'),
    path('jackets/<str:slug>/', get_jacket, name='jacket_url'),
    path('shirts/<str:slug>/', get_shirt, name='shirt_url'),
    path('pants/<str:slug>/', get_pants, name='pants_url'),
    path('accessories/<str:slug>/', get_accessories, name='accessory_url'),
    path('footwears/<str:slug>/', get_footwear, name='footwear_url'),

]
