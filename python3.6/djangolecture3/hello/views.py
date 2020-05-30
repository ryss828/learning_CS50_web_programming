from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world!")

def greet(request, someone):
    return HttpResponse("Hello, {}!".format(someone.capitalize()))