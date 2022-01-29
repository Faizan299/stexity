from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import context
from .models import Contact_Form
from .models import Post
from threading import Thread

from django.conf import settings
from django.core.mail import send_mail

def email():
    send_mail("Stexity","message","ha03172046587@gmail.com",['hyder.intel@gmail.com'])

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
        
        task1 = Thread(target=email)
        task1.start()
        task1.join()
        
    return render(request,'stexity_website/main.html', context)
