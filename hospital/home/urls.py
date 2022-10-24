from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', (views.index),name = 'home'),
    path('about',(views.about),name = 'about'),
    path('information',(views.information), name="information"),
    path('booking',(views.booking),name='booking'),
]