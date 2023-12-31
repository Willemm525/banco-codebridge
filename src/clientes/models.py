from django.db import models

# Create your models here.
class Cliente(models.Model):

    ESTADOS ={
        ('SP',"Sao Paulo"),
        ('MG',"Minas Gerais"),
        ('RJ',"Rio de Janeiro")
    }

    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    cidade = models.CharField(max_length=70, null=False, blank=False)
    estado = models.CharField(choices=ESTADOS,max_length=2,null=False,blank=False)
    endereco = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f'{self.nome} - {self.cidade}'