from django.db import models

# Create your models here.

class Customer(models.Model):

    GENRE = [
        ('feminin' , "Feminin"),
        ('masculin', "Masculin"),
    ]

    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date = models.DateField()
    genre = models.CharField(choices=GENRE, max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=50)  
    
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True, null=True)
    

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.nom

class User(models.Model):

    GENRE = [
        ('feminin' , "Feminin"),
        ('masculin', "Masculin"),
    ]

    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.DateField()
    genre = models.CharField(choices=GENRE, max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=50)  
    
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True, null=True)
    

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.nom        
