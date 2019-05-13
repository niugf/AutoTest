# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from wfmtest import models
from wfmtest.models import Casetask
from datetime import datetime
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponseRedirect
import json
from django.core import serializers


@csrf_exempt
def getform(request):
    if request.method == "POST":
        Casetask(
            title = request.POST.get('title',''),
            creater = request.POST.get('creater',''),
            email = request.POST.get('email',''),
            run_time = request.POST.get('runtime',''),
            case_path = request.POST.get('path', ''),
            desc = request.POST.get('desc', ''),
            timestamp = datetime.now(),
        ).save()
        return HttpResponseRedirect('/task') # 跳转到index界面
    return render_to_response('add.html')

def gettask(request):
    if request.method == "GET":
        data = {}
        tasklist =[]
        task = Casetask.objects.all()
        # 使用ORM
        # all()返回的是QuerySet 数据类型；values()返回的是ValuesQuerySet 数据类型
        data['list'] = json.loads(serializers.serialize("json", task))
        print(data)
        for i in data['list']:
            dic = i['fields']
            dic['cid'] = i['pk']
            tasklist.append(dic)

        print(tasklist)
        return render(request, 'manage.html', {
            'List': tasklist,
        })

    return render_to_response('manage.html')

def ajax_get(req):
    return render(req, 'manage.html')

def ajax_post(req):
    if req.method == 'POST':
        print(req.POST)
    else:
        print(req.GET)
    return HttpResponse('ajax_post')

@csrf_exempt
def delect(request):
    if request.method == "POST":
        id = request.POST.get('cids')
        ids = id.split(",")
        print(ids)
        for i in ids:
            models.Casetask.objects.filter(cid=i).delete()
        status = 1
        result = "true!"
        return HttpResponse(json.dumps({
            "status": status,
            "result": result
        }))

@csrf_exempt
def getlog(request):
    if request.method == "GET":
        data = {}
        tasklist =[]
        cid = request.GET.get("id")
        print(cid)
        log = models.Runlog.objects.filter(cid=cid)
        # 使用ORM
        # all()返回的是QuerySet 数据类型；values()返回的是ValuesQuerySet 数据类型
        data['list'] = json.loads(serializers.serialize("json", log))
        print(data)
        for i in data['list']:
            dic = i['fields']
            dic['id'] = i['pk']
            tasklist.append(dic)
        print(tasklist)
        return render(request, 'log.html', {
            'List': tasklist,
        })