from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    def __str__(self):
        return self.nome