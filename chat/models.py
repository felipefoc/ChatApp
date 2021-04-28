from django.db import models
from django.core import serializers
import json


class Sala(models.Model):
    name = models.CharField(max_length=20)
    members = models.IntegerField(default=0)

    def create_or_join(self, name):
        room = Sala.objects.get_or_create(name=name)
        object = Sala.objects.get(name=name)
        return object
    
    def add_member(self, name):
        object = Sala.objects.get(name=name)
        object.members += 1
        object.save()
    
    def remove_member(self, name):
        object = Sala.objects.get(name=name)
        object.members -= 1
        object.save()

    def get_room(self, name):
        room = Sala.objects.get(name=name)
        return room
    
    def online_users(self, room):
        object = Usuario()
        online = Usuario.objects.filter(sala=room)
        users = []
        for user in online:
            if user.username not in users:
                users.append(user.username)
        return users


    def __str__(self):
        return self.name
    

class Usuario(models.Model):
    username = models.CharField(max_length=20)
    sala = models.ForeignKey(Sala, verbose_name="sala", on_delete=models.CASCADE)

    def add_user(self, username, sala):
        user = Usuario.objects.get_or_create(username=username, sala=sala)
        object = Usuario.objects.get(username=username, sala=sala)
        return object
    
    def __str__(self):
        return self.username
    
