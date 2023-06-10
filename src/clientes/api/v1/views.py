from rest_framework import viewsets
from clientes.models import Cliente
from .serializers import ClienteSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

