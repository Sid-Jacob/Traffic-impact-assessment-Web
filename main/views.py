from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Form1.models import Form1
from Form2.models import Form2
from FormTemplate.models import FormTemplate
from Report.models import Report
from django.urls import reverse
import json
from django.db.models import Q
# 分页模块
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

# Create your views here.
# TODO
# login_url用reverse替换报错
# TODO
# 异步刷新订单，提交post请求字段刷新页面


@login_required(login_url="/accounts/login")
def gov(request):
    if request.method == 'POST':
        print("POST")
        #集采订单提交
        if request.POST.get('submit') == '提交集采订单':
            print("提交集采订单")
            province = request.POST.get('province', '')
            city = request.POST.get('city', '')
            county = request.POST.get('county', '')
            jicainum = request.POST.get('jicai-num', '')
            ddl = request.POST.get('jicai-ddl', '')
            negotiatetime = request.POST.get('jicai-negotiate', '')

            # 获取当前用户信息
            username = request.user  #得到用户名
            userId = request.session.get('_auth_user_id', None)  #得到用户id字段

            Form1.objects.create(province=province,
                                 city=city,
                                 county=county,
                                 number=jicainum,
                                 ddl=ddl,
                                 negotiateTime=negotiatetime,
                                 userId1=userId,
                                 userName1=username,
                                 subtype=1)
            return render(request, 'government.html')
        #评审订单提交
        elif request.POST.get('submit') == '提交评审订单':
            print("提交评审订单")
            ddl = request.POST.get('pingshen-ddl', '')
            num = request.POST.get('expert-num', '')
            price = request.POST.get('price', '')
            category = request.POST.get('expert-type', '')
            # 获取当前用户信息
            username = request.user
            userId = request.session.get('_auth_user_id', None)

            Form2.objects.create(expertCategory=category,
                                 price=price,
                                 expertNum=num,
                                 assessTime=ddl,
                                 userId1=userId,
                                 userName1=username,
                                 subtype=2)
            return render(request, 'government.html')
        else:
            return render(request, 'government.html')
    elif request.method == 'GET':
        u"""处理废除清单、刷新订单信息
            Method: GET
            params: 
                type  : method type(废除订单nullify1,nullify2+异步刷新/异步刷新2种订单信息update)
                id    : 订单 id
            return: json
        """
        # 刷新页面时也会调用GET方法，因此首次刷新可以不用js脚本在前端发请求
        print("get")
        # #创建json对象需要的数据
        # data = {}
        # data['status'] = 200
        # data['message'] = u'ok'
        # # 要显示的订单信息
        # data['form1list'] = []
        # data['formid'] = 0
        # data['percentage'] = 0
        # data['createTime'] = u""
        # data['form'] = u""  # form1和form2各个字段、接单用户

        page = request.GET.get('page', '')
        page2 = request.GET.get('page2', '')
        obj_type = request.GET.get('type', '')
        obj_id = request.GET.get('obj_id', '')
        user_id = request.session.get('_auth_user_id')
        user = request.user
        print("type:", obj_type, "obj_id:", obj_id, "user:", user, "user_id:",
              user_id)
        # gov/?type=nullify2&&obj_id=14
        if obj_id != '' and obj_type != '':
            # 废除订单
            print("nullify")
            obj_type = obj_type.lower()
            if obj_type == "nullify1":
                try:
                    l = Form1.objects.get(formId=obj_id)
                    l.significanceBit = False
                    l.save()
                except Exception as e:
                    pass
            elif obj_type == "nullify2":
                try:
                    l = Form2.objects.get(formId=obj_id)
                    l.significanceBit = False
                    l.save()
                except Exception as e:
                    pass
        # 统一更新订单
        if obj_type == ("update" or obj_type == "nullify1" or "nullify2"):
            pass
            # print("update")
            # rets1 = Form1.objects.filter(Q(userId1=user_id)).values_list(
            #     "province", "city", "county", "number", "ddl", "negotiateTime",
            #     "formId", "significanceBit", "taken", "done", "userId2",
            #     "userName2", "subtype").order_by("-formId")
            # rets2 = Form2.objects.filter(Q(userId1=user_id)).values_list(
            #     "expertCategory", "price", "expertNum", "assessTime", "formId",
            #     "significanceBit", "taken", "done", "userId2", "userName2",
            #     "subtype").order_by("-formId")
            # form1_list = []
            # for i in range(0, len(rets1)):
            #     form1_list.append(list(rets1[i]))
            # form2_list = []
            # for i in range(0, len(rets2)):
            #     form2_list.append(list(rets2[i]))

            # # TODO
            # # 翻页必须改成异步的
            # paginator = Paginator(form1_list, 3)  # 实例化Paginator, 每页显示3条数据
            # paginator2 = Paginator(form2_list, 3)

            # article = []
            # article2 = []

            # if page != '':
            #     try:
            #         article = paginator.page(page)
            #     # todo: 注意捕获异常
            #     except PageNotAnInteger:
            #         # 如果请求的页数不是整数, 返回第一页。
            #         article = paginator.page(1)
            #     except InvalidPage:
            #         # 如果请求的页数不存在, 重定向页面
            #         return HttpResponse('找不到页面的内容')
            #     except EmptyPage:
            #         # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            #         article = paginator.page(paginator.num_pages)
            # elif page2 != '':
            #     try:
            #         article = paginator2.page(page2)
            #     # todo: 注意捕获异常
            #     except PageNotAnInteger:
            #         # 如果请求的页数不是整数, 返回第一页。
            #         article = paginator2.page(1)
            #     except InvalidPage:
            #         # 如果请求的页数不存在, 重定向页面
            #         return HttpResponse('找不到页面的内容')
            #     except EmptyPage:
            #         # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            #         article = paginator2.page(paginator2.num_pages)
            # if page != '' or page2 != '':
            #     print("type article(page1):", type(article))

            #     print("Asy update")
            #     l = []
            #     l = User.objects.get(id=user_id)
            #     # TODO 增加分组权限显示
            #     if l.is_superuser == True:
            #         is_su = "是"
            #     else:
            #         is_su = "否"
            #     content = {
            #         "user_id": l.id,
            #         "username": l.username,
            #         "last_login": l.last_login.strftime("%Y-%m-%d %H:%M:%S"),
            #         "email": l.email,
            #         "date_joined": l.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
            #         "is_superuser": is_su,
            #         "page": article,
            #         "page2": article2,
            #     }
            #     return HttpResponse(json.dumps(content),
            #                         content_type="application/json")

        else:
            print("refresh")
            # 首次访问刷新页面
            # 处理集采订单翻页和首次更新
            rets1 = Form1.objects.filter(Q(userId1=user_id)).values_list(
                "province", "city", "county", "number", "ddl", "negotiateTime",
                "formId", "significanceBit", "taken", "done", "userId2",
                "userName2", "subtype").order_by("-formId")
            form1_list = []
            for i in range(0, len(rets1)):
                form1_list.append(list(rets1[i]))
            # TODO
            # 翻页必须改成异步的
            paginator = Paginator(form1_list, 3)  # 实例化Paginator, 每页显示3条数据

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

            # 处理评审订单翻页和首次更新
            rets2 = Form2.objects.filter(Q(userId1=user_id)).values_list(
                "expertCategory", "price", "expertNum", "assessTime", "formId",
                "significanceBit", "taken", "done", "userId2", "userName2",
                "subtype").order_by("-formId")
            form2_list = []
            for i in range(0, len(rets2)):
                form2_list.append(list(rets2[i]))
            # TODO
            # 翻页必须改成异步的
            paginator2 = Paginator(form2_list, 3)  # 实例化Paginator, 每页显示3条数据

            # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
            page2 = 1
            if request.method == "GET":
                page2 = request.GET.get('page2')
            try:
                article2 = paginator2.page(page2)
            # todo: 注意捕获异常
            except PageNotAnInteger:
                # 如果请求的页数不是整数, 返回第一页。
                article2 = paginator2.page(1)
            except InvalidPage:
                # 如果请求的页数不存在, 重定向页面
                return HttpResponse('找不到页面的内容')
            except EmptyPage:
                # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                article2 = paginator.page(paginator2.num_pages)
            try:

                print("try")
                l = []
                l = User.objects.get(id=user_id)
                # TODO 增加分组权限显示
                if l.is_superuser == True:
                    is_su = "是"
                else:
                    is_su = "否"
                content = {
                    "user_id": l.id,
                    "username": l.username,
                    "last_login": l.last_login.strftime("%Y-%m-%d %H:%M:%S"),
                    "email": l.email,
                    "date_joined": l.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
                    "is_superuser": is_su,
                    "page": article,
                    "page2": article2,
                }
                # print("content:", content)
            except Exception as e:
                #没有获取到对象
                print(e)
                pass

            # return redirect(reverse('main:gov') + "#tabs-2-3", content)
            return render(request, 'government.html', content)

    else:
        print("other")
        return render(request, 'government.html')
    # return render(request, 'government.html')


@login_required(login_url="/accounts/login")
def thirdParty(request):
    if request.method == 'POST':
        print("POST")
        #评审订单提交
        if request.POST.get('submit') == '提交抽审订单':
            print("评审")
            #向db写数据
            ddl = request.POST.get('pingshen-ddl', '')
            num = request.POST.get('expert-num', '')
            price = request.POST.get('price', '')
            category = request.POST.get('expert-type', '')

            # 获取当前用户信息
            username = request.user
            userId = request.session.get('_auth_user_id', None)

            # User.objects.create_user(username=user_name, password=pass_word_1)
            Form2.objects.create(expertCategory=category,
                                 price=price,
                                 expertNum=num,
                                 assessTime=ddl,
                                 userId1=userId,
                                 userName1=username,
                                 subtype=2)
            return render(request, 'Thirdparty.html')
        elif request.POST.get('submit') == '提交报告':
            print("上传交评报告")
            #向db写数据
            report = request.POST.get('report-content', 'xxx')
            print(report)
            formId = request.POST.get(
                'formId')  # 通过<input type="hidden" value="xxx">设置默认隐藏字段
            print(formId)
            form = Form1.objects.filter(Q(formId=formId))

            username = request.user
            userId = request.session.get('_auth_user_id', None)

            Report.objects.create(report=report,
                                  userId=userId,
                                  userName=username,
                                  formId=form[0])

            try:
                l = Form1.objects.get(formId=formId)
                l.done = True
                l.save()
            except Exception as e:
                pass
        return render(request, 'Thirdparty.html')
    elif request.method == 'GET':
        print("GET")
        u"""处理废除清单、刷新订单信息
            Method: GET
            params: 
                type  : method type(废除订单nullify2+异步刷新/异步刷新2种订单信息update/接单take)
                id    : 订单 id
            return: json
        """
        # 刷新页面时也会调用GET方法，因此首次刷新可以不用js脚本在前端发请求
        print("get")

        #获取新的数据和对应的对象，检查参数是否齐全？？？
        obj_type = request.GET.get('type', '')
        # obj_type = obj_type.lower()
        obj_id = request.GET.get('obj_id', '')
        user_id = request.session.get('_auth_user_id')
        username = request.user
        username = str(username)
        print("type:", obj_type, "obj_id:", obj_id, "user:", username,
              "user_id:", user_id)
        if obj_id != '' and obj_type != '':
            obj_type = obj_type.lower()
            print("nullify")
            # 废除订单
            if obj_type == "nullify2":
                print("nullify2")
                #获取Form2对象
                try:
                    l = Form2.objects.get(formId=obj_id)
                except Exception as e:
                    pass

                # 废除订单
                l.significanceBit = False
                l.save()
            elif obj_type == "take":
                print("take")
                #获取Form1对象
                try:
                    l = Form1.objects.get(formId=obj_id)
                    # 接单
                    l.taken = True
                    l.userId2 = user_id
                    l.userName2 = username
                    l.save()
                except Exception as e:
                    pass

        # 统一更新订单
        if obj_type == ("update" or "nullify1" or "nullify2" or "take"):
            pass
            # print("update")
            # rets1 = Form1.objects.filter(Q(userId1=user_id)).values_list(
            #     "province", "city", "county", "number", "ddl", "negotiateTime",
            #     "formId", "significanceBit", "taken", "done", "userId2",
            #     "userName2", "subtype").order_by("-formId")
            # rets2 = Form2.objects.filter(Q(userId1=user_id)).values_list(
            #     "expertCategory", "price", "expertNum", "assessTime", "formId",
            #     "significanceBit", "taken", "done", "userId2", "userName2",
            #     "subtype").order_by("-formId")
            # form1_list = []
            # for i in range(0, len(rets1)):
            #     form1_list.append(list(rets1[i]))
            # form2_list = []
            # for i in range(0, len(rets2)):
            #     form2_list.append(list(rets2[i]))

            # # TODO
            # # 翻页必须改成异步的
            # paginator = Paginator(form1_list, 3)  # 实例化Paginator, 每页显示3条数据
            # paginator2 = Paginator(form2_list, 3)
            # # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
            # page = 1
            # if request.method == "GET":
            #     page = request.GET.get('page')
            # try:
            #     article = paginator.page(page)
            # # todo: 注意捕获异常
            # except PageNotAnInteger:
            #     # 如果请求的页数不是整数, 返回第一页。
            #     article = paginator.page(1)
            # except InvalidPage:
            #     # 如果请求的页数不存在, 重定向页面
            #     return HttpResponse('找不到页面的内容')
            # except EmptyPage:
            #     # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            #     article = paginator.page(paginator.num_pages)
            # # context = {"page": article}
            # try:

            #     print("try")
            #     l = []
            #     l = User.objects.get(id=user_id)
            #     # TODO 增加分组权限显示
            #     if l.is_superuser == True:
            #         is_su = "是"
            #     else:
            #         is_su = "否"
            #     content = {
            #         "user_id": l.id,
            #         "username": l.username,
            #         "last_login": l.last_login.strftime("%Y-%m-%d %H:%M:%S"),
            #         "email": l.email,
            #         "date_joined": l.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
            #         "is_superuser": is_su,
            #         "page": article,
            #     }
            # except Exception as e:
            #     #没有获取到对象
            #     print(e)

            # #返回结果
            # return render(request, 'government.html', content)
            # # return HttpResponse(json.dumps(context),
            # #                     content_type="application/json")
        else:
            print("refresh")
            # 首次访问刷新页面
            user_id = request.session.get('_auth_user_id')
            user = request.user
            print("user:", user, "user_id:", user_id)
            # 处理集采订单翻页和首次更新
            # 正在进行的订单
            rets1 = Form1.objects.filter(
                Q(taken=True) & Q(done=False)
                & Q(significanceBit=True) & Q(userId2=user_id)).values_list(
                    "province", "city", "county", "number", "ddl",
                    "negotiateTime", "formId", "significanceBit", "taken",
                    "done", "userId2", "userName2",
                    "subtype").order_by("-formId")
            # 新订单
            rets2 = Form1.objects.filter(
                Q(taken=False) & Q(significanceBit=True)).values_list(
                    "province", "city", "county", "number", "ddl",
                    "negotiateTime", "formId", "significanceBit", "taken",
                    "done", "userId2", "userName2",
                    "subtype").order_by("-formId")
            # 已完成的订单
            rets3 = Form1.objects.filter(
                Q(done=True)
                & Q(significanceBit=True) & Q(userId2=user_id)).values_list(
                    "province", "city", "county", "number", "ddl",
                    "negotiateTime", "formId", "significanceBit", "taken",
                    "done", "userId2", "userName2",
                    "subtype").order_by("-formId")

            form1_list = []
            for i in range(0, len(rets1)):
                form1_list.append(list(rets1[i]))
            form2_list = []
            for i in range(0, len(rets2)):
                form2_list.append(list(rets2[i]))
            form3_list = []
            for i in range(0, len(rets3)):
                form3_list.append(list(rets3[i]))
            # TODO
            # 翻页必须改成异步的
            paginator = Paginator(form1_list, 3)  # 实例化Paginator, 每页显示3条数据

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

            paginator2 = Paginator(form2_list, 3)  # 实例化Paginator, 每页显示3条数据

            # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
            page2 = 1
            if request.method == "GET":
                page2 = request.GET.get('page2')
            try:
                article2 = paginator2.page(page2)
            # todo: 注意捕获异常
            except PageNotAnInteger:
                # 如果请求的页数不是整数, 返回第一页。
                article2 = paginator2.page(1)
            except InvalidPage:
                # 如果请求的页数不存在, 重定向页面
                return HttpResponse('找不到页面的内容')
            except EmptyPage:
                # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                article2 = paginator.page(paginator2.num_pages)

            paginator3 = Paginator(form3_list, 3)  # 实例化Paginator, 每页显示3条数据

            # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
            page3 = 1
            if request.method == "GET":
                page3 = request.GET.get('page3')
            try:
                article3 = paginator3.page(page3)
            # todo: 注意捕获异常
            except PageNotAnInteger:
                # 如果请求的页数不是整数, 返回第一页。
                article3 = paginator3.page(1)
            except InvalidPage:
                # 如果请求的页数不存在, 重定向页面
                return HttpResponse('找不到页面的内容')
            except EmptyPage:
                # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                article3 = paginator.page(paginator3.num_pages)

            # 第三方发起的评审订单
            rets4 = Form2.objects.filter(Q(userId1=user_id)).values_list(
                "expertCategory", "price", "expertNum", "assessTime", "formId",
                "significanceBit", "taken", "done", "userId2", "userName2",
                "subtype").order_by("-formId")
            form4_list = []
            for i in range(0, len(rets4)):
                form4_list.append(list(rets4[i]))
            print(form4_list)
            # TODO
            # 翻页必须改成异步的
            paginator4 = Paginator(form4_list, 3)  # 实例化Paginator, 每页显示3条数据

            # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
            page4 = 1
            if request.method == "GET":
                page4 = request.GET.get('page4')
            try:
                article4 = paginator4.page(page4)
            # todo: 注意捕获异常
            except PageNotAnInteger:
                # 如果请求的页数不是整数, 返回第一页。
                article4 = paginator4.page(1)
            except InvalidPage:
                # 如果请求的页数不存在, 重定向页面
                return HttpResponse('找不到页面的内容')
            except EmptyPage:
                # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                article4 = paginator4.page(paginator4.num_pages)

            try:

                print("try")
                l = []
                l = User.objects.get(id=user_id)
                # TODO 增加分组权限显示
                if l.is_superuser == True:
                    is_su = "是"
                else:
                    is_su = "否"
                content = {
                    "user_id": l.id,
                    "username": l.username,
                    "last_login": l.last_login.strftime("%Y-%m-%d %H:%M:%S"),
                    "email": l.email,
                    "date_joined": l.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
                    "is_superuser": is_su,
                    "page": article,
                    "page2": article2,
                    "page3": article3,
                    "page4": article4,
                }
                # print("content:", content)
            except Exception as e:
                #没有获取到对象
                print(e)
                pass

            return render(request, 'Thirdparty.html', content)

    else:
        print("other")
        return render(request, 'Thirdparty.html')


@login_required(login_url="/accounts/login")
def expert(request):
    if request.method == 'POST':
        print("POST")
        #评审订单提交
        if request.POST.get('submit') == '提交报告':
            print("上传交评报告")
            #向db写数据
            report = request.POST.get('report-content', 'xxx')
            print(report)
            formId = request.POST.get(
                'formId')  # 通过<input type="hidden" value="xxx">设置默认隐藏字段
            print(formId)
            form = Form2.objects.filter(Q(formId=formId))

            username = request.user
            userId = request.session.get('_auth_user_id', None)

            Report.objects.create(report=report,
                                  userId=userId,
                                  userName=username,
                                  formId=form[0])

            try:
                l = Form2.objects.get(formId=formId)
                l.done = True
                l.save()
            except Exception as e:
                pass
        return render(request, 'Expert.html')

    elif request.method == 'GET':
        print("GET")
        u"""处理刷新订单信息
            Method: GET
            params: 
                type  : take/update
                id    : 订单 id
            return: json
        """
        # 刷新页面时也会调用GET方法，因此首次刷新可以不用js脚本在前端发请求
        print("get")
        # #创建json对象需要的数据
        # data = {}
        # data['status'] = 200
        # data['message'] = u'ok'
        # # 要显示的订单信息
        # data['form1list'] = []
        # data['formid'] = 0
        # data['percentage'] = 0
        # data['createTime'] = u""
        # data['form'] = u""  # form1和form2各个字段、接单用户

        #获取新的数据和对应的对象，检查参数是否齐全？？？
        obj_type = request.GET.get('type', '')
        # obj_type = obj_type.lower()
        obj_id = request.GET.get('obj_id', '')
        user_id = request.session.get('_auth_user_id')
        username = request.user
        username = str(username)
        print("type:", obj_type, "obj_id:", obj_id, "user:", username,
              "user_id:", user_id)
        # 处理nullify和update命令，只相应ajax请求
        print("type:", obj_type, "obj_id:", obj_id, "user:", username,
              "user_id:", user_id)
        if obj_id != '' and obj_type != '':
            obj_type = obj_type.lower()
            # 接单
            if obj_type == "take":
                print("take")
                #获取Form1对象
                try:
                    l = Form2.objects.get(formId=obj_id)
                    # 接单
                    l.taken = True
                    l.userId2 = user_id
                    l.userName2 = username
                    l.save()
                except Exception as e:
                    pass
        # # 统一更新订单
        if obj_type != '' and (obj_type == "update"):
            pass
        #     print("update")
        #     rets = Form2.objects.filter(Q(userId1=user_id)).values_list(
        #         "expertCategory", "price", "expertNum", "assessTime", "formId",
        #         "significanceBit", "taken", "done", "userId2", "userName2",
        #         "subtype").order_by("-formId")

        #     form_list = []
        #     for i in range(0, len(rets)):
        #         form2_list.append(list(rets[i]))

        #     # TODO
        #     # 翻页必须改成异步的
        #     paginator = Paginator(form_list, 3)  # 实例化Paginator, 每页显示3条数据
        #     # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        #     page = 1
        #     if request.method == "GET":
        #         page = request.GET.get('page')
        #     try:
        #         article = paginator.page(page)
        #     # todo: 注意捕获异常
        #     except PageNotAnInteger:
        #         # 如果请求的页数不是整数, 返回第一页。
        #         article = paginator.page(1)
        #     except InvalidPage:
        #         # 如果请求的页数不存在, 重定向页面
        #         return HttpResponse('找不到页面的内容')
        #     except EmptyPage:
        #         # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        #         article = paginator.page(paginator.num_pages)
        #     # context = {"page": article}
        #     try:

        #         print("try")
        #         l = []
        #         l = User.objects.get(id=user_id)
        #         # TODO 增加分组权限显示
        #         if l.is_superuser == True:
        #             is_su = "是"
        #         else:
        #             is_su = "否"
        #         content = {
        #             "user_id": l.id,
        #             "username": l.username,
        #             "last_login": l.last_login.strftime("%Y-%m-%d %H:%M:%S"),
        #             "email": l.email,
        #             "date_joined": l.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
        #             "is_superuser": is_su,
        #             "page": article,
        #         }
        #     except Exception as e:
        #         #没有获取到对象
        #         print(e)

        #     #返回结果
        #     return render(request, 'Expert.html', content)
        #     # return HttpResponse(json.dumps(context),
        #     #                     content_type="application/json")
        else:
            print("refresh")
            # 首次访问刷新页面
            # 获取用户信息
            user_id = request.session.get('_auth_user_id')
            user = request.user
            print("user:", user, "user_id:", user_id)

            # 处理集采订单翻页和首次更新
            # 正在进行的订单
            rets1 = Form2.objects.filter(
                Q(userId2=user_id)
                & Q(significanceBit=True) & Q(done=False)).values_list(
                    "expertCategory",
                    "price",
                    "expertNum",
                    "assessTime",
                    "formId",
                    "significanceBit",
                    "taken",
                    "done",
                    "userId2",
                    "userName2",
                    "subtype",
                ).order_by("-formId")
            # 新订单
            rets2 = Form2.objects.filter(
                Q(taken=False) & Q(significanceBit=True)).values_list(
                    "expertCategory", "price", "expertNum", "assessTime",
                    "formId", "significanceBit", "taken", "done", "userId2",
                    "userName2", "subtype").order_by("-formId")
            # 已完成的订单
            rets3 = Form2.objects.filter(
                Q(userId2=user_id)
                & Q(significanceBit=True) & Q(done=True)).values_list(
                    "expertCategory", "price", "expertNum", "assessTime",
                    "formId", "significanceBit", "taken", "done", "userId2",
                    "userName2", "subtype").order_by("-formId")

            form1_list = []
            for i in range(0, len(rets1)):
                form1_list.append(list(rets1[i]))
            form2_list = []
            for i in range(0, len(rets2)):
                form2_list.append(list(rets2[i]))
            form3_list = []
            for i in range(0, len(rets3)):
                form3_list.append(list(rets3[i]))
            # TODO
            # 翻页必须改成异步的
            paginator = Paginator(form1_list, 3)  # 实例化Paginator, 每页显示3条数据

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

            paginator2 = Paginator(form2_list, 3)  # 实例化Paginator, 每页显示3条数据

            # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
            page2 = 1
            if request.method == "GET":
                page2 = request.GET.get('page2')
            try:
                article2 = paginator2.page(page2)
            # todo: 注意捕获异常
            except PageNotAnInteger:
                # 如果请求的页数不是整数, 返回第一页。
                article2 = paginator2.page(1)
            except InvalidPage:
                # 如果请求的页数不存在, 重定向页面
                return HttpResponse('找不到页面的内容')
            except EmptyPage:
                # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                article2 = paginator.page(paginator2.num_pages)

            paginator3 = Paginator(form3_list, 3)  # 实例化Paginator, 每页显示3条数据

            # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
            page3 = 1
            if request.method == "GET":
                page3 = request.GET.get('page3')
            try:
                article3 = paginator3.page(page3)
            # todo: 注意捕获异常
            except PageNotAnInteger:
                # 如果请求的页数不是整数, 返回第一页。
                article3 = paginator3.page(1)
            except InvalidPage:
                # 如果请求的页数不存在, 重定向页面
                return HttpResponse('找不到页面的内容')
            except EmptyPage:
                # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                article3 = paginator.page(paginator3.num_pages)

            try:

                print("try")
                l = []
                l = User.objects.get(id=user_id)
                # TODO 增加分组权限显示
                if l.is_superuser == True:
                    is_su = "是"
                else:
                    is_su = "否"
                content = {
                    "user_id": l.id,
                    "username": l.username,
                    "last_login": l.last_login.strftime("%Y-%m-%d %H:%M:%S"),
                    "email": l.email,
                    "date_joined": l.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
                    "is_superuser": is_su,
                    "page": article,
                    "page2": article2,
                    "page3": article3,
                }
                # print("content:", content)
            except Exception as e:
                #没有获取到对象
                print(e)
                pass

            return render(request, 'Expert.html', content)

    else:
        print("other")
        return render(request, 'Expert.html')