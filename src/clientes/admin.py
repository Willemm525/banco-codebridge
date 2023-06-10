from django.contrib import admin
from clientes.models import Cliente
from contas.models import Conta
# Register your models here.
class ContaInLine(admin.TabularInline):
    model = Conta
    min_num = 1
    extra = 1

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    inlines = [ContaInLine]