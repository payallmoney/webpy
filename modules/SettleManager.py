#coding:utf-8
import web
import utils
urls = (
  "", "settlemanager",
)
class settlemanager:
    def GET(self):
        return utils.render_template('settlemanager.html')

app_settlemanager = web.application(urls, locals())