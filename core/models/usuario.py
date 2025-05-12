from django.db import models

class Usuario(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nome
        
        