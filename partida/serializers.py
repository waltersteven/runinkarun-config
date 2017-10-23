from rest_framework.serializers import ModelSerializer
from .models import Partida

class PartidaSerializer(ModelSerializer):

    class Meta:
        model = Partida
        fields = '__all__'