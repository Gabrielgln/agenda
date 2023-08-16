from django.contrib import admin
from core.models import Evento

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    #para exibir na listagem o titulo, data do evento e data de criacao no admin
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    #para filtra por titulo no admin, sempre ter a virgula no final do filter
    list_filter = ('titulo',)
#comando para registra a model ao admin
admin.site.register(Evento, EventoAdmin)