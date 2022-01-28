from unicodedata import name
from django.shortcuts import render
from .models import Contact_Form
from .models import Post
from threading import Thread

from django.conf import settings
from django.core.mail import send_mail


def form(request):
    global message, email, name
    alldata = Post.objects.all()
    context = {'task': alldata}
    if request.method == 'POST':
        cont = Contact_Form()
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')
        cont.name = name
        cont.message = message
        cont.email = email
        cont.save()

        request.session['message'] = message

    t1 = Thread(target=run)
    t1.start()

    return render(request, 'stexity_website/main.html', context)


def run():
    global message, email, name
    message = message
    email = email
    name = name
    send_mail(name, message, email,['hyder.intel@gmail.com'])
