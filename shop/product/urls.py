from django.contrib import admin
from django.urls import path, include 
from .views import *

urlpatterns = [
    path('', index_page, name='index_page_url'),
    path('men/', men_page, name='men_url'),
    path('men/<str:slug>/', get_jacket, name='jacket_url'),

]
