from django.http import HttpResponse
from django.shortcuts import render
from .models import place


# Create your views here.
def demo(request):
    obj = place.objects.all()
    return render(request, "Home.html", {'result': obj})

def about(request):
    return render(request,"about.html")

def contact(request):
    return  render(request,"Contact.html")

def gallery(request):
    return render(request, "Gallery.html")

def Home(request):
    return render(request, "index.html")