from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Venda
from .models import Produto

def inicio(request):
    produtos= Produto.objects.order_by('idproduto')
    return render(request, 'shop/inicio.html', {'produtos':produtos})

def pag2(request, pk):
    post = get_object_or_404(Produto, pk=pk)
    return render(request, 'shop/pag2.html', {'post': post})