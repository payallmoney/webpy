#coding:utf-8
import web
import utils
import json
urls = (
  "/add.json","settlemanager_add_json",
  "/add","settlemanager_add",
  "", "settlemanager"
)
class settlemanager:
    def GET(self):
        return utils.render_template('settlemanager.html')
class settlemanager_add:
    def GET(self):
        return utils.render_template('settlemanager_add.html')
class settlemanager_add_json:
    returnobj = {"total":4,"rows":[   
            {"name":"姓名","value":"Bill Smith","group":"基本信息","editor":"text"},   
            {"name":"地址","value":"","group":"基本信息","editor":"text"},   
            {"name":"邮编","value":"123-456-7890","group":"基本信息","editor":"text"},   
            {"name":"邮箱","value":"bill@gmail.com","group":"联系方式","editor":{   
                "type":"combobox", 
                "options":{
                    "mode":"remote",
                    "url":"/options/drop",
                    "valueField":'value',   
                    "textField":'label',
                    "panelHeight":70
                }                
            }}   
        ]}
    def GET(self):
        web.header('Content-Type', 'application/json')
        return json.dumps(self.returnobj)
    def POST(self):
        web.header('Content-Type', 'application/json')
        return json.dumps(self.returnobj)
app_settlemanager = web.application(urls, locals())