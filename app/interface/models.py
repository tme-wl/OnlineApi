from django.db import models

# Create your models here.


class HostName(models.Model):
    """申请子域名"""
    name = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now=True)


class InterView(models.Model):
    """访问记录"""
    # 子域名
    hostname = models.ForeignKey(HostName, on_delete=models.CASCADE)
    # 方法 1，2，3，4 get post put delete
    method = models.IntegerField(default=1)
    # url name
    name = models.CharField(max_length=200)
    # json数据
    data = models.CharField(max_length=20480)
    # 创建时间
    create_time = models.DateTimeField(auto_now=True)
