from rest_framework.serializers import ModelSerializers
from core.models import Usuario

class UsuarioSerializer(ModelSerializers):
    class Meta:
        model = Usuario
        fields = "__all__"
        