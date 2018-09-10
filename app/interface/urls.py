from django.conf.urls import include, url
from django.contrib import admin
from interface import views

urlpatterns = [
    # 获取主页面接口
    url(r'^home$', views.home),
    # 申请子域名接口
    url(r'^subdomain$', views.subdomain),
    # 添加/获取/删除 接口数据
    url(r'^interface$', views.interface),

]
