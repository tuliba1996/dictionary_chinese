from django.db import models


class CharacterCommon(models.Model):
    id = models.AutoField(primary_key=True)
    chinese = models.CharField(max_length=255)
    pinyin = models.CharField(max_length=255)
    vietnamese = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.pinyin

