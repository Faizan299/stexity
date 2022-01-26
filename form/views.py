from tkinter.messagebox import RETRY
from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import context
from .models import Contact_Form
from .models import Post

def form(request):
    alldata = Post.objects.all()
    context = {'task': alldata}
    if request.method == 'POST':
        cont = Contact_Form()
        name=request.POST.get('name')
        message=request.POST.get('message')
        email=request.POST.get('email')
        cont.name=name
        cont.message=message
        cont.email=email
        cont.save()
    return render(request,'stexity_website/main.html', context)
