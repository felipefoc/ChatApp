from django.db import models
from django.db.models.deletion import CASCADE

class Usuario(models.Model):
    username = models.CharField(max_length=20)

    def add_user(self, username):
        return Usuario.objects.get_or_create(username=username)
    
    def remove_user(self, username):
        return Usuario.objects.get_or_404(username=username).delete()





class Sala(models.Model):
    name = models.CharField(max_length=20)
    online = models.ForeignKey(Usuario, on_delete=CASCADE)

    def join_room(self, name):
        sala = Sala.objects.get_or_create(name=name)
        
