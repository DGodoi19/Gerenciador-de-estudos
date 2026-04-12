from django.shortcuts import render, redirect, get_object_or_404
from .models import Trilha, Topico


def index(request):
    trilhas = Trilha.objects.all()
    return render(request, 'estudos/index.html', {'trilhas': trilhas})

def cadastro(request):
    if request.method == 'POST':
        nomeDaTrilha = request.POST.get("nomeDaTrilha")
        descricao = request.POST.get("descricao")
        semestre = request.POST.get("semestre")

        Trilha.objects.create(
            nomeDaTrilha = nomeDaTrilha,
            descricao = descricao,
            semestre = semestre
        )
        return redirect('index')
    return render(request, 'estudos/cadastro.html')


def detalhes_trilha(request, id):
    trilha = get_object_or_404(Trilha, id=id)
    topicos = Topico.objects.filter(trilha=trilha)
    return render(request, 'estudos/detalhes_trilha.html', {
        'trilha': trilha,
        'topicos': topicos
    })

def criar_topico(request, trilha_id):
    trilha = get_object_or_404(Trilha, id=trilha_id)
    if request.method == 'POST':
        nomeDoTopico = request.POST.get("nomeDoTopico")
        descricao = request.POST.get("descricao")

        Topico.objects.create(
            trilha=trilha,
            nomeDoTopico=nomeDoTopico,
            descricao=descricao
        )
        return redirect('detalhes_trilha', id=trilha_id)
    return render(request, 'estudos/criar_topico.html', {'trilha': trilha})

def marcar_como_concluido(request, topico_id):
    topico = get_object_or_404(Topico, id=topico_id)
    topico.concluido = True
    topico.save()
    return redirect('detalhes_trilha', id=topico.trilha.id)

def excluir_trilha(request, id):
    trilha = get_object_or_404(Trilha, id=id)
    trilha.delete()
    return redirect('index')

def excluir_topico(request, topico_id):
    topico = get_object_or_404(Topico, id=topico_id)
    trilha_id = topico.trilha.id
    topico.delete()
    return redirect('detalhes_trilha', id=trilha_id)

def editar_trilha(request, id):
    trilha = get_object_or_404(Trilha, id=id)
    if request.method == 'POST':
        trilha.nomeDaTrilha = request.POST.get("nomeDaTrilha")
        trilha.descricao = request.POST.get("descricao")
        trilha.semestre = request.POST.get("semestre")
        trilha.save()
        return redirect('detalhes_trilha', id=id)
    return render(request, 'estudos/editar_trilha.html', {'trilha': trilha})
