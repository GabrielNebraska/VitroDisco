from django.db import models

class Endereco(models.Model):

    #usuario = models.ForeignKey('usuario', on_delete=models.CASCADE, related_name='enderecos')
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.bairro}, {self.cidade}, {self.estado}, {self.cep}"