from django.db import models


# Create your models here.
class Task(models.Model):
    def __init__(self, _name, _isFinish):
        self.name = _name
        self.isFinish = _isFinish
        self.userList = []
        self.userNum = 0

    def addMember(self, _user):
        self.userList.append(_user)
        self.userNum += 1

    name = models.CharField(max_length=20)
    isFinish = models.CharField(max_length=3)



class Admin(models.Model):
    name = models.CharField(max_length=10)
    studentId = models.CharField(max_length=10)
    passwd = models.CharField(max_length=20)
    taskList = []


class User(models.Model):
    def __init__(self):
        self.taskList = []
        self.taskNum = 0

    def addTask(self, _task):
        self.taskList.append(_task)
        self.taskNum += 1

    name = models.CharField(max_length=10)
    studentId = models.CharField(max_length=10)
    passwd = models.CharField(max_length=20)
