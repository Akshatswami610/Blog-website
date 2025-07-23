from django.db import models
from django.utils import timezone
import secrets, string, datetime
from django.conf import settings
from django.contrib.auth.models import User


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # <--- FIXED
    content = models.TextField()
    image = models.ImageField(upload_to='blog/images', default="")
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_title


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    email=models.CharField(max_length=50,default="")
    subject=models.CharField(max_length=50, default="")
    message=models.CharField(default=500)
