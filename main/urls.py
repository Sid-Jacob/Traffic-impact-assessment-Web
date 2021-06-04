app_name = 'main'

from django.urls import path, re_path
from main import views

urlpatterns = [
    path('gov/', views.gov, name="gov"),
    path('thirdParty/', views.thirdParty, name="thirdParty"),
    path('expert/', views.expert, name="expert"),
    re_path(r'gov/.*?', views.gov),
    re_path(r'thirdParty/.*?', views.thirdParty),
    re_path(r'expert/.*?', views.expert),
]
