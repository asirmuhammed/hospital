from django.shortcuts import render
from . models import Booking

# Create your views here.
def index(request):
    return render (request,'index.html')
def about(request):
    return render(request,'about.html')    
def information(request):
    return render(request,'information.html')
def booking(request):
    dict_doc = {
        'doc' : Booking.objects.all()
    }
    return render(request,'booking.html',dict_doc)    