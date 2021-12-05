## backend

### 数据库相关

mysql安装：https://www.runoob.com/mysql/mysql-install.html

models中定义了数据库使用的模型；djangoProject下的settings定义数据库相关属性

<img src="https://user-images.githubusercontent.com/57995255/144731045-3b699ffa-30f3-4c9f-ae58-233bd1a5065d.png" width=300 alt="db"/>

数据库可使用可视化工具Navicat-for-Mysql查看；上述属性在连接时使用：

<img src="https://user-images.githubusercontent.com/57995255/144731230-5b2b7529-cf5e-4309-ac11-da1595ec08c8.png" width=300 alt="navicat"/>

#### models改动后需重新启动：

**删除migration/0001_initial.py**后

-python manage.py migrate; 

-python manage.py makemigrations wx_app; 

-python manage.py migrate wx_app;

### 接口相关

采用两级路径:djangoProject下urls和具体app下urls;总路径与前端指定url对应；前端访问路径时调用后端指定的函数(views中)

post:前端->后端；get:后端->前端；数据形式为json

后端(可以)使用rest Framework中的Response, 在localhost:8000/wx/../下可以查看传递的具体值：

<img src="https://user-images.githubusercontent.com/57995255/144731398-8edc0aa1-b16c-4b59-ab57-428961afd6e2.png" width=300 alt="rest"/>


添加应用时记得在settings的installed_apps中添加

