app_name = 'main'

from django.urls import path, re_path
from main import views

urlpatterns = [
    path('', views.distributer, name="main"),
    path('manager/', views.manager, name="manager"),
    path('gov/', views.gov, name="gov"),
    path('thirdParty/', views.thirdParty, name="thirdParty"),
    path('expert/', views.expert, name="expert"),
    re_path(r'manager/.*?', views.manager),
    re_path(r'gov/.*?', views.gov),
    re_path(r'thirdParty/.*?', views.thirdParty),
    re_path(r'expert/.*?', views.expert),
    path('init/', views.init, name="init"),
    re_path(r'init/.*?', views.init),
    path('delete/', views.delete, name="delete"),
    re_path(r'delete/.*?', views.delete),
]
