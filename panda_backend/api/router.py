from rest_framework import routers

from api.views import CharacterViewSet, TopicViewSet, CharacterInTopicViewSet, UserViewSet

router = routers.DefaultRouter()


router.register(r'character', CharacterViewSet)
router.register(r'topic', TopicViewSet, basename='topic')
router.register(r'words', CharacterInTopicViewSet)
router.register(r'user', UserViewSet)
