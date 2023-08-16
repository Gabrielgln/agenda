from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)
    #usando o usuario do admin
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

    #exigindo que a tabela se chame 'evento'
    class Meta:
        db_table = 'evento' 

    #função para exibir o titulo como nome do objeto principal
    def __str__(self):
        return self.titulo
    
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')
    
    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False
