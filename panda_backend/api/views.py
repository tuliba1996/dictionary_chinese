from rest_framework import viewsets, filters
# Create your views here.
from api.models import CharacterCommon, Topic, CharacterInTopic, User
from api.serializers import CharacterCommonSerializer, TopicSerializer, CharacterInTopicSerializer, \
    CustomObtainPairSerializer, UserSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView


class CharacterViewSet(viewsets.ModelViewSet):

    queryset = CharacterCommon.objects.all()
    serializer_class = CharacterCommonSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'chinese', 'pinyin', 'vietnamese')


class TopicViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    # queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def get_queryset(self, pk=None):
        user_id = self.request.GET.get('user', '')
        if user_id:
            query = Topic.objects.filter(user=user_id)
            return query
        return Topic.objects.all()


class CharacterInTopicViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = CharacterInTopic.objects.all()
    serializer_class = CharacterInTopicSerializer


class Login(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

