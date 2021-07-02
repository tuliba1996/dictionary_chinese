from django.db import models
from django.utils import timezone
from api.models import User


class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name


class CharacterInTopic(models.Model):
    id = models.AutoField(primary_key=True)
    chinese = models.CharField(max_length=255)
    pinyin = models.CharField(max_length=255)
    vietnamese = models.CharField(max_length=255, blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now, editable=False)
