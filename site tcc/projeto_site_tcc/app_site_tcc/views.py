from django.shortcuts import render
from .models import Comentario

def home(request):
    return render(request,'comentarios/home.html')

def comentarios(request):
    # Salvar os dados da tela para o banco de dados
    novo_comentario = Comentario()
    novo_comentario.nome = request.POST.get('nome')
    novo_comentario.comentario = request.POST.get('comentario')
    novo_comentario.save()
    # Exibir todos os comentarios já cadastrados em uma nova página
    comentarios = {
        'comentarios': Comentario.objects.all()
    }
    
    # Retornar os dados para a página de listagem de usuários
    return render(request,'comentarios/comentarios.html',comentarios)
