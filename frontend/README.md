## frontend

### 部署

在微信开发者工具或uniapp中使用；

Appid: wx30d9b9b18cffedc7

对应原型，前端结构:

+ login

+ home 
  + addTask      
  + submitTask
      
+ folder

+ manage 
  + addMember
  + delMember
  + setAdmin
  + changePasswd
        
+ finance 
  + flow
  + publicity
  + uploadInfo

### 接口

使用request与访问url：method确定数据传输方向；data为向后端传递；success中res.data为向前端传递；

http://127.0.0.1:8000/wx/.../

### 其他

wxml中bindtap绑定js中函数；

onload()初始化页面；navigateTo页面转换；

添加新页面时在app.json的pages中添加；
         
