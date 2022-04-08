from django.conf import settings
from django.db import models
from django.utils import timezone

#exemplo de instrucoes
# Produto.objects.filter(idproduto=x)
# Post.objects.filter(title__contains='title')
# Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

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
        self.data = timezone.now()
        self.save()

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.PositiveIntegerField(default=999999)
    estoque = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(blank=True,null=True)
    idproduto = models.PositiveIntegerField(default=0)


    def subtrai(self,venda):
        self.estoque = self.estoque - venda

    def publish(self):
        self.save()

    def __str__(self):
        return self.nome

