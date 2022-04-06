from django.shortcuts import render
from django.utils import timezone
from .models import Venda
from .models import Produto

def inicio(request):
    produtos= Produto.objects.order_by('idproduto')
    return render(request, 'shop/inicio.html', {'produtos':produtos})