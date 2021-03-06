#-*-coding:utf-8 -*-
import web
import modules.main
import modules.SettleManager
import modules.CostManager
import modules.SysManager
import modules.Options
import utils
urls = (
  "/main", modules.main.app_main,
  "/settlemanager", modules.SettleManager.app_settlemanager,
  "/costmanager", modules.CostManager.app_costmanager,
  "/sysmanager", modules.SysManager.app_sysmanager,
  "/options", modules.Options.app_options,
  "/(.*)", "index"
)

class index:
    def GET(self,url):
        return utils.render_template('login.html')

app = web.application(urls, locals())

if __name__ == "__main__":
    app.run()