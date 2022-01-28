from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from django.db import models
from PIL import Image
from django.shortcuts import render



class Contact_Form(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    desc = models.TextField()
    image = models.ImageField(upload_to='images')


    def save(self):
        super().save()


        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

        def __str__(self):
            return self.name

      
