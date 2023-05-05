"""
为项目配置ASGI

它将ASGI可调用对象公开为 ”application“的模块变量
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'untitled.settings')

application = get_asgi_application()

