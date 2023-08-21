from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image


class JobPost(models.Model):
    Jobname = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to='job/%Y%m%d/', blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.Jobname


class Management(models.Model):
    Management_Job = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to='Management_Job/%Y%m%d/', blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.Management_Job


class Sales(models.Model):
    Sales_Job = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to='Sales_Job/%Y%m%d/', blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.Sales_Job


class Other(models.Model):
    Other_Job = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to='Sales_Job/%Y%m%d/', blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.Other_Job
