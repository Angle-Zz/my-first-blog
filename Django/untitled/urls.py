"""
项目的url配置

'urlpatterns' 列表将网址路由到视图
有关更多信息，请参阅：https://docs.djangoproject.com/en/4.2/topics/http/urls/

例子：
函数视图
    1. 添加导入：从my_app导入视图
    2. 向网址模式添加一个 URL：path（''， views.home， name='home'）
基于类的视图
    1.添加导入：从other_app.views导入主页
    2. 添加一个网址到网址模式： path（''， Home.as_view）， name='home'）
包括另一个网址
    1. 导入 include（） 函数：从 django.urls 导入包含，路径
    2. 向网址模式添加一个 URL：path（'blog/'， include（'blog.urls'））
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]


