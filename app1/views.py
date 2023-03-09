from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def leo(request):
    return HttpResponse('<h1>bloody sweet</h1>')


def rolex(request):
    return HttpResponse('<h2>vaadiki life time settlement raaa </h2>')

def vikram(request):
    return HttpResponse('<h1><marquee>Ika   MOdhaledadhaaama</h1></marquee>')

