from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from PIL import Image



class VideoList(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to='doctor/%Y%m%d/', blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name