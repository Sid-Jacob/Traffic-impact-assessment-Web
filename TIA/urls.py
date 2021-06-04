"""TIA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Django后台管理页面
    # re_path(r'^login/.*?$', include('login.urls', namespace='login')),
    # 直接改setting里的login_url
    re_path(r'accounts/', include('login.urls', namespace='login')),
    path('', views.index, name='home'),
    re_path(r'index/.*?', views.index, name='index'),
    path('main/', include('main.urls', namespace='main')),
    path('spider/', views.spider, name='spider'),

    # test
    path('news/', views.news, name='news'),
    path('news_list/', views.news_list),
    path('search_list/', views.search_list),
    # path('logout/', views.logout),
    path('', include('Comment.urls', namespace='Comment')),
    path('likes/', include('Likes.urls', namespace='Likes')),
]
