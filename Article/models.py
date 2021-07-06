from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils.timezone import now

from django.apps import AppConfig

# Create your models here.


# TODO 修改date为时间类型
class Article(models.Model):
    # STATUS_CHOICES = (
    #     ('d', '草稿'),
    #     ('p', '发表'),
    # )
    # article_id = models.CharField(verbose_name='标号', max_length=100)
    # null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空，那么在新建一个model对象的时候是不会报错的！！
    # blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填，比如 admin 界面下增加 model 一条记录的时候。直观的看到就是该字段不是粗体。
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标题', max_length=100)
    link = models.CharField(verbose_name="原始url",
                            blank=True,
                            null=True,
                            max_length=1000)
    imglink = models.CharField(verbose_name="图片url",
                               blank=True,
                               null=True,
                               max_length=1000)
    essay = models.TextField(verbose_name='正文', blank=True, null=True)
    # status = models.CharField(verbose_name='状态',
    #                           max_length=1,
    #                           choices=STATUS_CHOICES,
    #                           default='p')
    # views = models.PositiveIntegerField(verbose_name='浏览量', default=0)
    date = models.CharField(verbose_name="新闻日期",
                            blank=True,
                            null=True,
                            max_length=100)

    # TimeStamp = models.DateTimeField(auto_now_add=True)

    # category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE, blank=False, null=False)
    # tags = models.ManyToManyField(Tag, verbose_name='标签集合', blank=True)

    # 使对象在后台显示更友好
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return r"/news/?id=" + str(self.id)

    # # 更新浏览量
    # def viewed(self):
    #     self.views += 1
    #     self.save(update_fields=['views'])

    # # 下一篇
    # def next_article(self):  # id比当前id大，状态为已发布，发布时间不为空
    #     return Article.objects.filter(id__gt=self.id,
    #                                   status='p',
    #                                   pub_time__isnull=False).first()

    # # 前一篇
    # def prev_article(self):  # id比当前id小，状态为已发布，发布时间不为空
    #     return Article.objects.filter(id__lt=self.id,
    #                                   status='p',
    #                                   pub_time__isnull=False).first()

    class Meta:
        # ordering = ['-created_time']  # 按文章创建日期降序
        verbose_name = '文章'  # 指定后台显示模型名称
        verbose_name_plural = '文章列表'  # 指定后台显示模型复数名称
        db_table = 'Article'  # 数据库表名
        # get_latest_by = 'created_time'