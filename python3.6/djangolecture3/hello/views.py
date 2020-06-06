from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world!")

def render_template(request):
    return render(request, "hello/rend_temp.html")

def render_template2(request, someone):
    return render(request, "hello/rend_temp2.html", {
        "name": someone.capitalize()
    })
