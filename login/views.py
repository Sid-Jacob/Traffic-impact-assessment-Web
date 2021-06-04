from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# 认证模块
from django.contrib import auth
# 对应数据库
from django.contrib.auth.models import User

# Create your views here.

# TODO
# 忘记密码
# TODO
# 登录后跳转到之前的页面、根据用户信息跳转到个人主页


#登出
def logout(request):
    auth.logout(request)
    return redirect(reverse("home"))


#登录、注册页
def login(request):
    # return redirect(".")
    print("login")
    if request.method == 'POST':
        print("POST")
        #登录表单提交
        if request.POST.get('submit') == 'sign_in':  # get->name字段，返回值->value字段
            print("signin")
            #从db读数据
            user_name = request.POST.get('login-name', '')
            pass_word = request.POST.get('login-password', '')
            print(user_name)
            print(pass_word)

            # User.objects.create(username=user_name, password=pass_word)
            user_obj = auth.authenticate(username=user_name,
                                         password=pass_word)
            print("user_obj:", user_obj)
            if not user_obj:
                print("login failed")
                # return redirect(".")
                return render(request, "login.html")
            else:
                auth.login(request, user_obj)  #开启会话
                print("login successfully")
                #如果是从需要权限访问的资源处跳转进入登录页面，则登录后返回之前的页面，而不是index
                # 根据登录的用户信息跳转到个人主页
                path = request.GET.get("next", "") or "index/"
                print(path)
                return redirect(path)
                # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                # return render(request, "Index.html")
                # print(reverse("index"))
                # return redirect(reverse("index"))
                # https://zhuanlan.zhihu.com/p/139292329
                # return render(request, "Index.html")  # 为什么会无效？？？

        #注册表单提交
        elif request.POST.get('submit') == 'sign_up':
            print("signup")
            #向db写数据
            user_name = request.POST.get('register-name', '')
            pass_word_1 = request.POST.get('register-password', '')
            pass_word_2 = request.POST.get('confirm-password', '')
            if (pass_word_1 != pass_word_2):
                print("密码不一致")
                return redirect('.', {'error': '两次密码请输入一致'})
            else:
                print("signup succ")
                # User.objects.create(username=user_name, password=pass_word_1) # 旧版本明文存密码，但auth.authenticate函数会算哈希比对
                User.objects.create_user(username=user_name,
                                         password=pass_word_1)
                # https://www.cnblogs.com/Zzbj/p/9984783.html
                # https://blog.csdn.net/qq_33445330/article/details/92078480?
                path = request.GET.get("next", "") or "index/"
                print(path)
                return redirect(path)
        else:
            return render(request, 'login.html')
    else:
        print("other")
        return render(request, 'login.html')
