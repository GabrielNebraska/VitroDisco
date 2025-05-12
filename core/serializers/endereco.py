from rest_framework.serializers import ModelSerializers
from core.models import Endereco

class EnderecoSerializer(ModelSerializers):
    class Meta:
        model = Endereco
        fields = "__all__"