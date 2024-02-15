from django.db import models

# Create your models here.
from django.db.models import Model


class Blog(models.Model):
    image = models.ImageField(upload_to='blog/image', default='download.png')
    title = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
