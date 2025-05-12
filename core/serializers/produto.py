from rest_framework.serializers import ModelSerializers
from core.models import Produto

class ProdutoSerializer(ModelSerializers):
    class Meta:
        model = Produto
        fields = "__all__"