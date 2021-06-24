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
    qualified = models.IntegerField(default=-1)  # 专家审核集采报告合格位(-1/0/1)
    need_examine = models.BooleanField(
        default=False)  # 提交报告后根据percentage判断是否需要抽检
    form2_send = models.BooleanField(default=False)  # 是否已经由平台管理员发起抽检订单
