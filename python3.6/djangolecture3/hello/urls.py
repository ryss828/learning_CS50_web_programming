from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rentemp", views.render_template, name="render_template"),
    path("<str:someone>", views.render_template2, name="render_template2"),
]
