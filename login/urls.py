app_name = 'login'

from django.urls import path, re_path
from login import views

urlpatterns = [
    re_path(r'login/.*?', views.login, name="login"),
    re_path(r'logout/.*?', views.logout, name="logout"),
]
