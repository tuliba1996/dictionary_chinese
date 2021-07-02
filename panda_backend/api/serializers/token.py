from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class CustomObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):

        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data.pop('refresh', None)  # remove refresh from the payload
        # data['token'] = str(refresh.access_token)

        # Add extra responses here
        data['email'] = self.user.email
        data['name'] = self.user.first_name
        data['id'] = self.user.id
        data['username'] = self.user.username
        # data['kind'] = self.user.kind
        # data['date'] = datetime.date.today()
        return data

