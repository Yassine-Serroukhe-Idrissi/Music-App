from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MusicInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    music_aut = models.CharField(max_length=60, null=True, blank=True)
    music_titre = models.CharField(max_length=60, null=False, blank=False)
    music_image = models.ImageField(null=True, blank=True)
    music_audio = models.FileField(null=False)

    def __str__(self):
        return self.music_titre + ' ' + self.music_aut

