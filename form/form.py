from django import forms
from django.contrib.auth.models import User
from django.db import models


class UserRegisterForm(forms.Form):
    name = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()