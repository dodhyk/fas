from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(response):
    return render(response, "home.html") 

def klub(response):
    return render(response, "klub/klub.html")

def inputklub(response):
    return render(response, "klub/inputklub.html")

def editklub(response):
    return render(response, "klub/editklub.html")

def pemain(response):
    return render(response, "pemain/pemain.html")

def inputpemain(response):
    return render(response, "pemain/inputpemain.html")

def editpemain(response):
    return render(response, "pemain/editpemain.html")

def liga(response):
    return render(response, "liga/liga.html")

def inputliga(response):
    return render(response, "liga/inputliga.html")

def editliga(response):
    return render(response, "liga/editliga.html")