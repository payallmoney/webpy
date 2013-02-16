#-*-coding:utf-8 -*-
import web
import login
import utils
urls = (
  "/login", login.app_login,
  "/", "index"
)

class index:
    def GET(self):
        return utils.render_template('index.html')

app = web.application(urls, locals())

if __name__ == "__main__":
    app.run()