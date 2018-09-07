from django.shortcuts import render

# Create your views here.
import uuid
import json
from django.shortcuts import render
from django.http import HttpResponse
from interface.models import InterView, HostName
from django.conf import settings


def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError:
        return False
    except:
        return False
    return True


def Response(msg):
    return HttpResponse(json.dumps(msg), content_type="application/json")


def home(request):
    if request.method == 'GET':
        # 获取主页面
        return render(request, 'home.html')


def subdomain(request):
    if request.method == 'POST':
        # 申请子域名
        print(request.body, 'request.body')
        if request.body:
            data = json.loads(request.body)
        else:
            data = {}
        subdomain_name = data.get('subdomain', '')
        if not subdomain_name:
            subdomain_name = str(uuid.uuid1())
            subdomain_name = ''.join(subdomain_name.split('-'))
        if not subdomain_name.isalnum():
            return Response({
                "msg": "申请子域名非法",
                "status": 500,
            })
        objs = HostName.objects.filter(name=subdomain_name)
        if objs:
            return Response({
                "msg": "申请失败,子域名暂时重复",
                "status": 500
            })
        obj = HostName()
        obj.name = subdomain_name
        obj.save()
        return Response({
            "msg": "添加子域名成功",
            "status": 200,
            "data": {"subdomain": subdomain_name}
        })


def interface(request):
    if request.method == 'GET':
        METHOD = {
            1: "GET",
            2: "POST",
            3: "PUT",
            4: "DELETE"
        }
        # 获取当前接口
        subdomain = request.GET.get('subdomain', '')
        if not subdomain:
            return Response({
                "msg": "传入参数错误，暂时没有此子域名申请",
                "status": 500
            })
        try:
            hostnames = HostName.objects.get(name=subdomain)
        except HostName.DoesNotExist:
            return Response({
                "msg": "传入参数错误，暂时没有此子域名申请",
                "status": 500
            })
        objs = InterView.objects.filter(hostname=hostnames)
        data = []
        for obj in objs:
            data.append({
                "id": obj.id,
                "url": METHOD[obj.method] + ": http://" + settings.WEBDOMAIN + "/" + subdomain + '/' + obj.name,
                "data": obj.data
            })
        return Response({
            "msg": "获取数据成功",
            "data": data,
            "status": 200
        })
    elif request.method == 'POST':
        if request.body:
            request_data = json.loads(request.body)
        else:
            request_data = {}

        # 提交新接口数据
        data = request_data.get('data', '')
        method = request_data.get('method', 0)
        subdomain = request_data.get('subdomain', '')
        name = request_data.get('name', '')
        if not data or not method or not subdomain or not name:
            return Response({
                "msg": "传入参数错误",
                "status": 500,
            })
        try:
            subdomain_instance = HostName.objects.get(name=subdomain)
        except HostName.DoesNotExist:
            return Response({
                "msg": "子域名传入错误",
                "status": 500
            })
        try:
            eval(data)
        except:
            return Response({
                "msg": "传入数据格式错误",
                "status": 500
            })
        obj = InterView()
        obj.method = method
        obj.name = name
        obj.data = data
        obj.hostname = subdomain_instance
        obj.save()
        return Response({
            "msg": "存入参数成功",
            "status": 200
        })
    elif request.method == 'DELETE':
        request_data = json.load(request.body)
        id = request_data.get('id', 0)
        try:
            obj = InterView.objects.get(id=id)
        except InterView.DoesNotExist:
            return Response({
                "msg": "获取数据失败",
                "status": 500
            })
        obj.delete()
        return Response({
            "msg": "删除成功",
            "status": 200
        })

def api(request, pk):
    {
        "a": 1,
        "b": 2
    }
    return HttpResponse("Hello, world. You're at the polls index.")