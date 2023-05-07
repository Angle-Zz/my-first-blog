from django.urls import path, re_path
from . import views
"""
正则表达式：
^ 表示文本的开始
$ 表示文本的结束
\d 表示数字
+ 表示前面的元素应该重复至少一次
() 用来捕捉模式中的一部分
"""

urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
]
