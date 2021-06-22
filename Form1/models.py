from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from FormTemplate.models import FormTemplate


# Create your models here.
class Form1(FormTemplate):
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    number = models.IntegerField()
    ddl = models.DateField(auto_now_add=False)
    negotiateTime = models.DateField(auto_now_add=False)
    percentage = models.IntegerField()
