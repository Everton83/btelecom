from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.db.models.fields import DateTimeField

# Create your models here.

ELEMENTOS=(
    ("Crossconennect","Crossconennect"),
    ("Mimo","Mimo"),
    ("Diplexer","Diplexer"),
    ("Triplexer","Triplexer"),
    ("Quadriplexer","Quadriplexer"),
    ("Mixmode","Mixmode"),
    ("Powersplit","Powersplit"),
    ("Radio Compartilhada","Radio Compartilhada"),
    ("Mais Elementos","Mais Elementos"),
)

class Solucoes(models.Model):
    titulo = models.CharField(max_length=200)
    numero = models.PositiveIntegerField(unique=True)
    elementos = models.CharField(max_length=50,choices=ELEMENTOS)
    portas = models.PositiveIntegerField()
    descricao = models.CharField(max_length=200)
    image = models.ImageField(upload_to="produtos")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Solucoes" + str(self.id)