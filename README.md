## Django命令

cd TIA

`python manage.py runserver`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py startapp [appname]`

一定要去setting.py里注册

## 常用正则表达式

`(.*?) 匹配所有字符串`

`([\s\S]*) 但是如果带换行符会失效，如果需要匹配包括换行符，则使用`

(images/.*?.jpg)

{%static $1%}

("images.*?.\....") {%static $1%}

("css.*?.\....")

("js.*?.\...")

使用正则表达式匹配

\{%static (.*?)%\}

https://www.cnblogs.com/jerryqi/p/9604828.html

http://www.dongchuanmin.com/archives/471.html

### Bugs & Solutions

第三方提交报告formId字段和订单号不匹配
专家提交报告formId字段和订单号不匹配
报告textarea字段无法修改

--》form的id重复了


只剩一个订单时操作错误

--》console.log(result.page[0][x])


一个页面有多个表单要提交，第一个表单之外的表单require字段已填写但显示“未填写”

---

### TODO：

#### main
TODO 异步翻页
TODO: bug:异步更新时progress-bar无法正常渲染，时间显示格式和普通刷新不一样

#### Comment
TODO 未登录状态发表Comment有bug
TODO 为什么发完评论没有自动刷新页面，news模板中修改文本框，以及ajax提交评论方式，异步刷新

#### Login
TODO 忘记密码
TODO 登录后跳转到之前的页面、根据用户信息跳转到个人主页

#### TIA
TODO 搜索文章、订单