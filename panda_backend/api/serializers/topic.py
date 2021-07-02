from rest_framework import serializers

from api.models import Topic, CharacterInTopic, User


# class TopicUserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    # user = TopicUserSerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ('user', 'name', 'description', 'id', 'created')


class CharacterInTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterInTopic
        fields = '__all__'


