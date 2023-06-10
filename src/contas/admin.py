from django.contrib import admin
from .models import Conta

# Register your models here.
@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    pass