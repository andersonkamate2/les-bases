from django.contrib.auth.models import AbstractUser
from django.db import models


class Connexion(AbstractUser):
    pass
# Create your models he
class Etudiant(models.Model):
    nom = models.CharField(max_length=20)
    post_nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    sexe = models.CharField(max_length=6)
    nationalite = models.CharField(max_length=50)
    date_naiss = models.DateTimeField()
    province = models.CharField(max_length=20)
    territoire = models.CharField(max_length=20)
    commune = models.CharField(max_length=20)
    ville = models.CharField(max_length=20)
    Quartier = models.CharField(max_length=20)
    Avenu = models.CharField(max_length=20)
    numero = models.IntegerField()




