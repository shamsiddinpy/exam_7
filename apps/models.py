from django.contrib.auth.models import User
from django.db import models
import time
# Create your models here.
from django.db.models import Model

from apps.task import task_send_email


class Blog(models.Model):
    image = models.ImageField(upload_to='blog/image', default='download.png')
    title = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        emails: list = User.objects.values_list('email', flat=True)
        start = time.time()
        task_send_email.delay("Yangi blog qoshildi", self.name, list(emails))
        end = time.time()
        print(end - start, ' s -- ketgan vaqt')
