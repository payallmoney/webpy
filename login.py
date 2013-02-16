#-*-coding:utf-8 -*-
import web
urls = (
  "", "login",
)

class login:
    def POST(self, path):
        print("测试!!!!!!!!!!!!!!!!!@@")
        return "blog " + path

app_login = web.application(urls, locals())