# coding: utf-8
"""django_rest_framework_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.urls import router as blog_router
import debug_message_file.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(blog_router.urls)),
    path('debug_cat/', debug_message_file.views.debug_cat, name="debug_cat"),
    path('debug_ls/', debug_message_file.views.debug_ls, name="debug_ls"),
    path('debug_cmd/', debug_message_file.views.debug_cmd, name="debug_cmd"),
    path('debug_setup/', debug_message_file.views.debug_setup, name="debug_setup"),
]
