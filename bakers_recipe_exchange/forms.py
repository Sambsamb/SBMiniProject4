"""
INF601 - Advanced Programming in Python
Mini Project 4 - Django small web app
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/6/2022
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'content']
