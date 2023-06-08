from django.db import models
from datetime import datetime
from django import forms

# Create your models here.

class Machine(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False)
        
    nom= models.CharField(
        max_length= 200
    )

    def __str__(self):
        return str(self.id) + "->" + self.nom

    def get_name(self):
        return str(self.id) + " " + self.nom

class Machine(models.Model):

    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=6)
    maintenanceDate = models.DateField(default=datetime.now())
    Type = models.CharField(max_length=32, choices=TYPE, default='PC')

class Personne(models.Model):
    
    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=6)
    prenom = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id) + "->" + self.nom

    def get_name(self):
        return str(self.id) + " " + self.nom

    def get_surname(self):
        return str(self.id) + " " + self.prenom

class LoginForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

class Infrastructure(models.Model):
    nom = models.CharField(max_length=200)
    machines = models.ManyToManyField(Machine)

    def __str__(self):
        return self.nom

class Commutateur(models.Model):

    id = models.AutoField(
        primary_key=True,
        editable=False)
        
    nom= models.CharField(
        max_length= 200
    )

    def __str__(self):
        return str(self.id) + "->" + self.nom

    def get_name(self):
        return str(self.id) + " " + self.nom

class Maintenance(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()