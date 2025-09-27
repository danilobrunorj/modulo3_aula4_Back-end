from django.contrib import admin
from .models import Clientes

@admin.register(Clientes)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'idade', 'ativo')

    search_fields = ('nome', 'email')

