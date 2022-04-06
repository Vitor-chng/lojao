from django import forms

from .models import Produto
from .models import Venda

class CriaVenda(forms.ModelForm):

    class Meta:
        model = Venda
        fields = ('nome', 'cpf','email','endereco','idproduto','quantidade')


class CriaProduto(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ('nome', 'preco','estoque','imagem','idproduto')


        