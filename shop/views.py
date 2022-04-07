from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .forms import CriaVenda
from .forms import CriaProduto,EditaProduto
from django.utils import timezone
from .models import Venda
from .models import Produto

def menu(request):
    produtos= Produto.objects.order_by('idproduto')
    vendas= Venda.objects.order_by('idproduto')
    context={'produtos':produtos,'vendas':vendas}
    return render(request,'shop/menu.html',context)

def gerencias(request):

    produtos=Produto.objects.all()
    context={'produtos':produtos}
    return render(request,'shop/gerencias.html',context)

def catalogos(request):

    produtos=Produto.objects.all()
    context={'produtos':produtos}
    return render(request,'shop/catalogos.html',context)

def gerencia(request,pk):

    produtos=get_object_or_404(Produto, pk=pk)
    context={'produtos':produtos}
    return render(request,'shop/gerencia.html',context)

def catalogo(request,pk):

    produtos=get_object_or_404(Produto, pk=pk)
    context={'produtos':produtos}
    return render(request,'shop/catalogo.html',context)

def compra(request,pk):
    produtos=get_object_or_404(Produto, pk=pk)
    form = CriaVenda()
    context={'form': form,'produtos':produtos}
    #arg=pk
    return render(request, 'shop/compra.html', context)
   # redirect(reverse('final', arg))

def edicao(request,pk):
    
    produtos=get_object_or_404(Produto, pk=pk)
    form = EditaProduto()
    context={'produtos':produtos,'form': form}
    return render(request,'shop/edicao.html',context)


def final(request,arg):
    produtos=get_object_or_404(Produto, pk=arg)
    context={'produtos':produtos}
    return render(request,'shop/final.html',context)


def adiciona(request):
    
    form = CriaProduto()
    context={'form': form}
    return render(request,'shop/adiciona.html',context)