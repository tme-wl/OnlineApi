from django.db import models

# Create your models here.


class Message(models.Model):
    """消息存储"""
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=2048)
    create_time = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='weixin/')