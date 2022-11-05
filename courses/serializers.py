from rest_framework import serializers

from . import models


class GameSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = '__all__'


class GameListSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = ['id', 'name']
