"""
INF601 - Advanced Programming in Python
Mini Project 4 - Django small web app
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/6/2022
"""

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the Baker's Recipe Exchange index.")
