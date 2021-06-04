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