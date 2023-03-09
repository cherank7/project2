from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def santhaanam(request):
    return HttpResponse('<h1>never say to die</h1>')

def amar(request):
    return HttpResponse('<h2>once upon time there lived a ghost')

def vikram(request):
    return HttpResponse('<h1><marquee>padhaa choosukundham</h1></marquee>')