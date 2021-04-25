from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def room(request, room_name, user_name):
    return render(request, 'room.html', {
        'room_name': room_name,
        'user_name': user_name,
    })
