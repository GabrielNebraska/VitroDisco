from rest_framework.serializers import ModelSerializers
from core.models import Usuario

class ProdutoSerializer(ModelSerializers):
    class Meta:
        model = Usuario
        fields = "__all__"