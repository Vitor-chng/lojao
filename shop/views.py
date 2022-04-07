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
   # produtos=Produto.objects.all()
    context={'produtos':produtos}
    return render(request,'shop/gerencias.html',context)

def catalogos(request):
    produtos=Produto.objects.filter(estoque__gt=0)
   # produtos=Produto.objects.all()
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
    if request.method == "POST":
        form = CriaVenda(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.data = timezone.now()
            if( ((produtos.estoque - post.quantidade)>=0)):
                post.valortotal = produtos.preco * post.quantidade
                produtos.estoque = produtos.estoque - post.quantidade
                post.save()
                produtos.save()
                return redirect('final',post.valortotal)
            else:
                return redirect('erro')
    else:
        form = CriaVenda()
        context={'form':form}
    return render(request, 'shop/compra.html',context)

def edicao(request,pk):
    
    produtos=get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = EditaProduto(request.POST, instance=produtos)
        if form.is_valid():
            produtos = form.save(commit=False)
            produtos.save()
            return redirect('gerencia', pk=produtos.pk)
    else:
        form = EditaProduto(instance=produtos)
    return render(request, 'shop/edicao.html', {'form': form})

def final(request,arg):
    print(arg)
    var1=arg
    return render(request,'shop/final.html',{'var1':var1})

def adiciona(request):
    if request.method == "POST":
        form = CriaProduto(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.data = timezone.now()
            post.idproduto = 1
            post.save()
            return redirect('gerencias')
    else:
        form = CriaProduto()
        context={'form':form}
    return render(request, 'shop/adiciona.html',context)

def erro(request):
    return render(request,'shop/erro.html')