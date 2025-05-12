from rest_framework.viewsets import ModelViewSet
from core.models import Produto
from core.serializers.produto import ProdutoSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    