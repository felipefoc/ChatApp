from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
class Produtos():
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor



def index(request):
    return render(request, 'index.html')

def room(request, room_name, user_name):
    return render(request, 'room.html', {
        'room_name': room_name,
        'user_name': user_name,
    })



def ajax_view(request):
    return render(request, 'produtos.html')

def create_product(request, nome, valor):
    instance = Produtos(
        nome=nome,
        valor=valor
    )
    instance.create()
    return HttpResponse(204)
