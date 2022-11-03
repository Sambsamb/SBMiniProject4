"""
INF601 - Advanced Programming in Python
Mini Project 4 - Django small web app
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/6/2022
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]