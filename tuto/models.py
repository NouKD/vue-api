from django.db import models


# Create your models here.

class Utilisateur(models.Model):
    nom = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=8)
    email = models.EmailField()
    phone = models.CharField(max_length=8)
    image = models.ImageField(upload_to='profile/', default='useravatar.png')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)