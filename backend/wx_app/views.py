import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from wx_app.models import *

# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User

current_studentId = ""


class login(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        tmpId = request.data["id"]
        tmpPasswd = request.data["passwd"]
        idList = list(User.objects.all().values("studentId"))
        print(idList)
        # user = authenticate(studentId=tmpId, passwd=tmpPasswd)
        if {"studentId": tmpId} in idList:
            obj = User.objects.get(studentId=tmpId)
            if tmpPasswd == obj.passwd:
                global current_studentId
                current_studentId = obj.studentId
                print(current_studentId)
                print("login success")
            else:
                print("wrong passwd")
        else:
            print("invalid id")

        return Response({"status": True})

    def get(self, request, *args, **kwargs):
        print(request.data)
        return Response({"status": True})


class addMember(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        tmpName = request.data["name"]
        tmpId = request.data["id"]
        tmpPasswd = request.data["passwd"]
        idList = list(User.objects.all().values("studentId"))
        print(idList)
        if {"studentId": tmpId} in idList:
            print("user exists")
        else:
            User.objects.create(name=tmpName, studentId=tmpId, passwd=tmpPasswd)
            print("add success")

        return Response({"status": True})


class delMember(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        tmpName = request.data["name"]
        nameList = list(User.objects.all().values("name"))
        print(nameList)
        if {"name": tmpName} in nameList:
            User.objects.filter(name=tmpName).delete()
            print("del success")
        else:
            print("no member")

        return Response({"status": True})


class setAdmin(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        tmpName = request.data["name"]
        nameList = list(Admin.objects.all().values("name"))
        print(nameList)
        if not nameList:
            obj = User.objects.get(name=tmpName)
            Admin.objects.create(name=tmpName, studentId=obj.studentId, passwd=obj.passwd)
            print("add admin success")
        else:
            Admin.objects.delete()
            obj = User.objects.get(name=tmpName)
            Admin.objects.create(name=tmpName, studentId=obj.studentId, passwd=obj.passwd)
            print("replace admin success")

        return Response({"status": True})


class changePasswd(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        tmpOldPwd = request.data["oldPwd"]
        tmpNewPwd1 = request.data["newPwd1"]
        tmpNewPwd2 = request.data["newPwd2"]
        print(current_studentId)
        if tmpNewPwd1 == tmpNewPwd2:
            obj = list(User.objects.filter(studentId=current_studentId))[0]
            if obj.passwd == tmpOldPwd:
                User.objects.filter(studentId=current_studentId).update(passwd=tmpNewPwd1)
                print("change passwd success")
            else:
                print("wrong old passwd")
        else:
            print("different new passwd")

        return Response({"status": True})


taskList = [
    {'content': '任务1', "members": "a", "edit": "y"},
    {'content': '任务2', "members": "a,b", "edit": "y"},
    {"content": "任务3", "members": "a,b,c", "edit": "n"},
]
userTaskList = [
    {"content": "任务1", "edit": "y"},
    {"content": "任务2", "edit": "y"},
    {"content": "任务3", "edit": "n"},
]


class delTask(APIView):
    def post(self, request, *args, **kwargs):
        tmpIndex = int(request.data["index"])
        print(tmpIndex)
        global taskList
        del taskList[tmpIndex]
        print(taskList)

        return Response({"status": True})

    def get(self, request, *args, **kwargs):
        taskListJson = json.dumps(taskList, ensure_ascii=False)
        print(taskListJson)
        userTaskListJson = json.dumps(userTaskList, ensure_ascii=False)
        print(userTaskListJson)
        tasks = {"taskList": taskList, "userTaskList": userTaskList}
        return Response(tasks)
