from django.conf import settings
from django.db import models
from django.utils import timezone

class Venda(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    data = models.DateTimeField(default=timezone.now)
    idproduto = models.PositiveIntegerField(default=0)
    quantidade = models.PositiveIntegerField(default=0)
    valortotal = models.PositiveIntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.cpf


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.PositiveIntegerField(default=999999)
    estoque = models.PositiveIntegerField(default=0)
    imagem = models.CharField(max_length=200)
    idproduto = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return self.idproduto