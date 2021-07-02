from rest_framework import serializers

from api.models import CharacterCommon


class CharacterCommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterCommon
        fields = '__all__'

