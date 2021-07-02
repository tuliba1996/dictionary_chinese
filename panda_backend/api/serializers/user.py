from rest_framework import serializers
from api.models import User, UserProfile



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('title', 'address')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.title = profile_data.get('title', profile.title)
        profile.save()

        return instance

