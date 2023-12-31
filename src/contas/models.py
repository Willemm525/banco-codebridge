from django.db import models

# Create your models here.
class Conta(models.Model):
    cliente = models.ForeignKey('clientes.Cliente',
                                null=True,
                                on_delete=models.SET_NULL)
    saldo = models.DecimalField('Saldo do cliente',
                                max_digits=12,
                                decimal_places=2,
                                default=0)
    data_abertura = models.DateTimeField(auto_now_add=True, 
                                        null=False)

    def __str__(self):
        return f"{self.cliente.nome} - R${self.saldo}"