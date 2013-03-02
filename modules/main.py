#coding:utf-8
import web
import utils
urls = (
  "", "main",
)
class main:
    def GET(self):
        raise web.seeother('../')
    def POST(self):
        data = web.input()
        print(data)
        param = {'username':data.username,'password':data.password}
        ret = utils.db.users.find(param)
        print(ret.count())
        flag = True if ret.count()>0 else False 
        print(flag)
        if flag:
            return utils.render_template('main.html',msg=u'密码正确',**data)
        else:
            return utils.render_template('login.html',msg=u'密码错误',**data)

app_main = web.application(urls, locals())