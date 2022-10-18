from django.http import HttpResponse
from django.shortcuts import render

def Index(request):
    return render(request,"Index.html")

def About(request):
    return render(request,"About.html")