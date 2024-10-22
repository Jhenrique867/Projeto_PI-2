from django.db import models

class Usuario(models.Model):

    id_usuario = models.AutoField(primary_key=True)
    nome_usuario = models.TextField(max_length=255)
    sobrenome_usuario = models.TextField(max_length=255)
    email = models.EmailField(unique=True)