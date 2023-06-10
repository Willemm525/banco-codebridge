from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('clientes', views.ClientViewSet, basename='clientes')