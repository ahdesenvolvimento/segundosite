from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoModelForm, ContatoForm
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        'produtos':Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    if str(request.user) != 'AnonymousUser':
        form = ContatoForm(request.POST or None)
        if str(request.method) == 'POST':
            if form.is_valid():
                messages.success(request, 'E-mail enviado com sucesso!')
                form = ContatoForm()
            else:
                messages.error(request,'Erro ao enviar o e-mail')
        context = {
            'form':form
        }
        return render(request, 'contato.html', context)
    else:
        redirect('ops')

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'Sucesso!')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro!')
        else:
            form = ProdutoModelForm()
        context = {
            'form':form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('ops')

def ops(request):
    return render(request, 'ops.html')