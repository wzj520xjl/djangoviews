import hashlib
import random

import time
from django.http import HttpResponse
from django.shortcuts import render

from App.models import UserModel


def index(request):
    print(request)
    return HttpResponse('index')


def user_zhuce(request):
    if request.method == 'GET':
        return render(request,'user_zhuce.html')
    elif request.method == 'POST':
        username = request.POST.get('username')

        user = UserModel()
        user.u_name = username
        token = genrate_token(request.META.get('REMDTE_ADDR'))
        user.u_token = token

        user.save()

        response = HttpResponse('注册成功')
        response.set_cookie('token',token)
        return response
def genrate_token(ip):
    t = time.time()
    r = random.random()

    before = str(t)+str(ip)+str(r)
    print(before)

    md5 = hashlib.md5()
    md5.update(before.encode('utf-8'))
    return md5.hexdigest()


def user_login(request):
    if request.method == 'GET':
        return render(request,'ueer_login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        users = UserModel.objects.filter(u_name=username)

        if users.exists():
            user = users.first()
            token = genrate_token(request.META.get('REMDTE_ADDR'))
            user.u_token = token
            user.save()
            response = HttpResponse('用户登录成功')
            response.set_cookie('token',user.u_token)
            return response
        else:
            return HttpResponse('登录用户不存在')



def user_zhongxin(request):
    token = request.COOKIES.get('token')
    if not token:
        return render(request, 'user_zhongxin.html')
    else:
        user = UserModel.objects.get(u_token=token)
        username = user.u_name

        return render(request,'user_zhongxin.html',context={'username':username})


def user_logout(request):
    response = HttpResponse('退出成功')
    response.delete_cookie('token')
    return response


def user_infor(request):
    u_token = request.COOKIES.get('token')
    if not u_token:
        return HttpResponse("用户已退出")
    try:
        user = UserModel.objects.get(u_token=u_token)
        username = user.u_name
        token = user.u_token
        return render(request,'user_infor.html',{'username':username,'token':token})
    except Exception as e:
        return HttpResponse('用户已被强制下线')