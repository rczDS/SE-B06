from wx_app import views
from django.contrib import admin
from django.urls import path


# 'wx_app/'即为二级路径
urlpatterns = [
    path('wx_login/', views.login.as_view()),
    path('wx_addMember/', views.addMember.as_view()),
    path('wx_delMember/', views.delMember.as_view()),
    path('wx_setAdmin/', views.setAdmin.as_view()),
    path('wx_changePasswd/', views.changePasswd.as_view()),
    path('wx_delTask/', views.delTask.as_view()),
]
