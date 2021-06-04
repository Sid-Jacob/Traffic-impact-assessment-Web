from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from FormTemplate.models import FormTemplate
# Create your models here.


class Report(models.Model):
    reportId = models.AutoField(primary_key=True)
    report = models.TextField(null=False)
    # userId1 = models.ForeignKey(User,
    # on_delete=models.CASCADE,
    # related_name='id')
    userId = models.IntegerField(verbose_name="报告撰写用户id",
                                 null=False,
                                 blank=False)
    userName = models.CharField(max_length=100,
                                null=False,
                                blank=False,
                                default="default-username")
    createTime = models.DateTimeField(auto_now_add=True)  # 订单发布时间
    formId = models.ForeignKey(FormTemplate, on_delete=models.CASCADE)
