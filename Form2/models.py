from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from FormTemplate.models import FormTemplate


# Create your models here.
class Form2(FormTemplate):
    expertCategory = models.CharField(max_length=100)  # ABC
    price = models.IntegerField()
    expertNum = models.IntegerField()
    assessTime = models.DateField(auto_now_add=False)
