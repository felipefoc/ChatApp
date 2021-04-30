from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Sala

# Create your views here.

def index(request):
    rooms = Sala.objects.filter(members__gt=0)
    Sala.objects.filter(members__lt=1).delete()
    
    return render(request, 'index.html', {
        'rooms': rooms,
    })
def room(request, room_name, user_name):
    if ' ' in user_name and  ' ' in room_name:
        return redirect('/')
    
    return render(request, 'room.html', {
        'room_name': room_name,
        'user_name': user_name,
    })
