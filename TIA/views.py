from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# from . import models  #同一个包下的import方式，（要有__init__.py文件存在）
from django.http import HttpResponse
# 认证模块
from django.contrib import auth
# 对应数据库
from django.contrib.auth.models import User
import Article
from Article import models
import Comment
# from Comment import models
from Comment.forms import CommentForm
import Likes
# 正则表达式
import re
# 分页模块
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.db.models import Q
import os
from django.contrib.contenttypes.models import ContentType


def home(request):
    return redirect(reverse("index"))


# TODO 搜索文章、订单


def index(request):
    # 首页展示最新的5条新闻（暂时用id最大的5条，之后改为TimeStamp最新 ### ）
    # news = models.Article.objects.values_list("id", "title").order_by(
    #     "-id")  # 查询所有，按照新鲜程度降序排列
    # news1 = []
    # for i in range(0, min(5, len(news))):
    #     news1.append(list(news[i]))
    #     news1[i][0] = r"/news/?id=" + str(news1[i][0])
    #     print(news1[i][1])
    # return render(request, 'index.html', {'data': news1})

    # 全部的article数据
    news_obj = models.Article.objects.values_list("id", "title",
                                                  "imglink", "date").order_by(
                                                      "-id")  # 查询所有，按照新鲜程度降序排列
    news_list = []
    # print((news_obj[0]))
    del_list = []
    for i in range(0, len(news_obj)):
        news_list.append(list(news_obj[i]))
        news_list[i][0] = r"/news/?id=" + str(news_list[i][0])
        for j in range(0, len(news_list[i])):
            # 删除掉图片显示异常的新闻
            if news_list[i][j] == "":
                del_list.append(i)

    del_list = del_list[::-1]
    for i in del_list:
        if i < len(news_list):
            del news_list[i]
    # 处理搜索文章请求
    if request.method == 'GET':
        #登录表单提交
        if request.GET.get('submit') == '搜索':
            #从db读数据
            keyword = request.GET.get('keyword', '')
            #多个字段模糊查询， 括号中的下划线是双下划线，双下划线前是字段名，双下划线后可以是icontains或contains,区别是是否大小写敏感，竖线是或的意思
            return redirect('../search_list/?keyword=' + keyword)

    paginator = Paginator(news_list, 3)  # 实例化Paginator, 每页显示5条数据
    # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
    page = 1
    if request.method == "GET":
        page = request.GET.get('page')
    try:
        article = paginator.page(page)
    # todo: 注意捕获异常
    except PageNotAnInteger:
        # 如果请求的页数不是整数, 返回第一页。
        article = paginator.page(1)
    except InvalidPage:
        # 如果请求的页数不存在, 重定向页面
        return HttpResponse('找不到页面的内容')
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        article = paginator.page(paginator.num_pages)
    context = {"page": article}
    return render(request, "Index.html", context)


def news(request):  #GET方法参数如何传递？？？***
    #data直接为/news/之后的全部内容？？？
    #1.从主页点击列表访问，直接以url方式（GET）判断是那篇新闻(暂时使用id作为标识，之后改为TimeStamp ### )(不用判断是不是GET方式传参数？？？)
    #2.若直接访问/news/则返回第一篇新闻
    # print(data, '\n')
    id = 1
    if request.method == 'GET':
        id = request.GET.get('id', '')
    # id = int(re.findall(r"\d+", data)[0])

    # response = models.Article.objects.get(id=id)
    post = get_object_or_404(Article.models.Article, id=id)
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()  #为什么能用set_all函数？？？***

    #response只能在.html中用.进行title，imglink等的读取，不能在这里读
    # title = response['title']
    # essay = response['essay']
    # imglink = response['imglink']

    # 图片暂时采用网络上现成的图片，如果需要本地图片，只需要将图片放到images文件夹并改变网页代码
    context = {
        'data': post,
        'form': form,
        'comment_list': comment_list,
    }
    #从db读数据
    return render(request, 'news.html', context)


def spider(request):
    os.system('python spider.py')
    return redirect(reverse('index'))


# 以下函数未使用
def news_list(request):
    # 全部的article数据
    news_obj = models.Article.objects.values_list("id", "title").order_by(
        "-id")  # 查询所有，按照新鲜程度降序排列
    news_list = []
    # print((news_obj[0]))
    for i in range(0, len(news_obj)):
        news_list.append(list(news_obj[i]))
        news_list[i][0] = r"/news/?id=" + str(news_list[i][0])
    # 处理搜索文章请求
    if request.method == 'GET':
        #登录表单提交
        if request.GET.get('submit') == '搜索':
            #从db读数据
            keyword = request.GET.get('keyword', '')
            #多个字段模糊查询， 括号中的下划线是双下划线，双下划线前是字段名，双下划线后可以是icontains或contains,区别是是否大小写敏感，竖线是或的意思
            return redirect('../search_list/?keyword=' + keyword)

    paginator = Paginator(news_list, 3)  # 实例化Paginator, 每页显示5条数据
    # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
    page = 1
    if request.method == "GET":
        page = request.GET.get('page')
    try:
        article = paginator.page(page)
    # todo: 注意捕获异常
    except PageNotAnInteger:
        # 如果请求的页数不是整数, 返回第一页。
        article = paginator.page(1)
    except InvalidPage:
        # 如果请求的页数不存在, 重定向页面
        return HttpResponse('找不到页面的内容')
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        article = paginator.page(paginator.num_pages)
    context = {"page": article}
    return render(request, "news_list.html", context)


def search_list(request):
    # 处理搜索文章请求
    if request.method == 'GET':
        #从db读数据
        keyword = request.GET.get('keyword', '')
        if keyword != "" and keyword != None:
            # 模糊查询？？？***
            # 多个字段模糊查询， 括号中的下划线是双下划线，双下划线前是字段名，双下划线后可以是icontains或contains,区别是是否大小写敏感，竖线是或的意思
            rets = models.Article.objects.filter(
                Q(essay__icontains=keyword) | Q(title__icontains=keyword)
                | Q(date__icontains=keyword)
                | Q(id__icontains=keyword)).values_list(
                    "id", "title").order_by("-id")
            news_list = []
            for i in range(0, len(rets)):
                news_list.append(list(rets[i]))
                news_list[i][0] = r"/news/?id=" + str(news_list[i][0])

            paginator = Paginator(news_list, 3)  # 实例化Paginator, 每页显示3条数据
            # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
            page = 1
            if request.method == "GET":
                page = request.GET.get('page')
            try:
                article = paginator.page(page)
            # todo: 注意捕获异常
            except PageNotAnInteger:
                # 如果请求的页数不是整数, 返回第一页。
                article = paginator.page(1)
            except InvalidPage:
                # 如果请求的页数不存在, 重定向页面
                return HttpResponse('找不到页面的内容')
            except EmptyPage:
                # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                article = paginator.page(paginator.num_pages)
            context = {"page": article, "keyword": keyword}
            return render(request, "search_list.html", context)
    return redirect("../news_list/")
