# -*- coding:UTF-8 -*-
import requests
import pytest
import json
import Model.request_xl as request_xl
import os
import platform
import configparser


class requestAPI(object):
    # init
    def __init__(self, log,conf_Filename,section=None):
        self.t_headers = None
        self.log = log
        self.cr = configparser.ConfigParser()
        self.section = section
        self.conf_Filename = conf_Filename

    # ###############################################
    #
    # 请求接口 如果kwargs不为空，则为case需要传递的参数
    # 请求接口 如果需要取活的url，可以传入可变参数args
    ##################################################

    def execute(self, caseFileName, sheetname, ApiPurpose,*args,**kwargs):
        try:
            # 读取case配置文件并获得对应值
            rxl = request_xl.request_xl(caseFileName, self.log)
            api_values = rxl.get_xl(sheetname, ApiPurpose)
            self.API_Host = api_values[2]

            ##可变传入url为元祖的[0]#########
            if args == ():
                self.Request_URL= api_values[3]
            else:
                self.Request_URL = args[0]

                print(args[0])

            self.Request_Method = api_values[4]
            self.extra = api_values[12]
            self.is_header = api_values[7]

            ####可变传入request data 为json####
            if kwargs == {}:
                if api_values[6] == "{}":
                    self.Request_Data = "{}"
                else:
                    self.Request_Data = eval(api_values[6])
            else:
                self.Request_Data = kwargs

                print(self.Request_Data)



            # 检查结果点
            self.code = api_values[8]
            t_url = self.API_Host + self.Request_URL

            if self.is_header == "Yes":
                # 获取cookies
                config_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/configure/'+ self.conf_Filename
                if 'Windows' in platform.system():
                    # windows os
                    config_path = config_path.replace('/', '\\')
                self.cr.read(config_path,encoding="utf-8-sig")
                cookies = self.cr.get(self.section, "cookies")
                t_headers = {
                    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36",
                    "Cookie": cookies
                }

                # 打印执行的用例
                self.log.info("Start" + " " + "Request" + " " + t_url)
                if self.Request_Data == "{}":
                    response = requests.request(self.Request_Method, t_url, headers=t_headers)
                else:
                    response = requests.request(self.Request_Method, t_url, headers=t_headers, data=self.Request_Data)
                self.log.info("HTTP 返回值：" +  str(response.status_code))
                self.log.info("校验返回JSON：" + self.extra)
                if response.status_code == self.code:
                # 直接返回json
                # return response.text
                    if self.extra == "No":
                        return response
                    else:
                        api_result = json.loads(response.text)
                        return api_result
                else:
                    self.log.info("错误码为：%d"%(response.status_code))
                    self.log.info("错误返回为：%s"%(response.text))
                    print("错误码为：%d"%(response.status_code))
                    pytest.fail("case"+ "-"+ ApiPurpose + "-"+"error")

            else:
                t_headers = self.t_headers
                response = requests.request(self.Request_Method, t_url, headers=t_headers, data=self.Request_Data)
                # 直接返回response
                return response

        except Exception as e:
            self.log.info("===== request API error =====%s" % e)
            pytest.fail("CASE FAIL")
            return 0

