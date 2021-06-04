from django.conf.urls import include, url
from Likes import views
#http://localhost:8000/likes/ +
#在project的urls.py导入整个url配置
app_name = 'Likes'
urlpatterns = [
    url(r'^likes_change$', views.likes_change, name='likes_change'),
    url(r'^likes_nums$', views.likes_nums, name='likes_nums'),
]