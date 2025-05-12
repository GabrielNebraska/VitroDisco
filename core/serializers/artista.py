from rest_framework.serializers import ModelSerializers
from core.models import Artista

class ArtistaSerializer(ModelSerializers):
    class Meta:
        model = Artista
        fields = "__all__"