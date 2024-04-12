from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm


# Create your views here.
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
        return render(request, 'cadastrar_produto.html', {'form': form})
    
def reajustar_produto(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'reajustar_produto.html', {'form': form, 'produto': produto})

def reabastecer_produto(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    if request.method == 'POST':
        quantidade = int(request.POST['quantidade'])
        produto.quantidade_em_estoque += quantidade
        produto.save()
        return redirect('lista_produtos')
    return render(request, 'reabastecer_produto.html', {'produto': produto})

