from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class FormTemplate(models.Model):
    formId = models.AutoField(primary_key=True)
    subtype = models.IntegerField(null=False, blank=False, default=1)
    # userId1 = models.ForeignKey(User,
    # on_delete=models.CASCADE,
    # related_name='id')
    userId1 = models.IntegerField(verbose_name="发起订单用户id",
                                  null=False,
                                  blank=False)
    userName1 = models.CharField(max_length=100,
                                 null=False,
                                 blank=False,
                                 default="default-username")
    createTime = models.DateTimeField(auto_now_add=True)  # 订单发布时间
    significanceBit = models.BooleanField(default=True)  # 订单有效位，政府用户废除订单用
    taken = models.BooleanField(default=False)  # 是否已被接单
    done = models.BooleanField(default=False)  # 订单是否已完成

    # userId2 = models.ForeignKey(User,
    #                             on_delete=models.CASCADE,
    #                             related_name='id')
    userId2 = models.IntegerField(verbose_name="接单用户id", null=True, blank=True)
    userName2 = models.CharField(max_length=100, null=True)
