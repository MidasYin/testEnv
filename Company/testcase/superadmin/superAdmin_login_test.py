import requests
import os
from Model.request_API import requestAPI
from Model.config import Configure
from Model.Logger import Logger
import platform
import pytest

class Test_Login:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_login(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        conf = Configure(path)

        try:
            conf_filename = "superAdmin.ini"
            Request = requestAPI(log,conf_filename)
            log.info("Superadmin 进行登录：")
            res = Request.execute("config_superAdmin.xlsx","checkLogin","login_superAdmin")
            log.info(str(res.status_code))
            if res.status_code == 200:
                cookies = requests.utils.dict_from_cookiejar(res.cookies)  # 返回值 jessionid
                result=res.json() #返回值 json
                role = result["data"]["role"]
                user_id = (result["data"]["user_id"])
                #处理cookies格式
                key = cookies["SESSION"]
                cookies = "SESSION" + "=" + key
                #把cookies传递出去,后续请求使用
                log.info("cookies="+ cookies)

                conf.Set("login","cookies",cookies) # 设置 setion、option、value
                conf.Set("login","role",str(role))
                conf.Set("login","user_id",str(user_id))

        except Exception as  e:
            log.error("=====case error ====%s" % e)
            pytest.fail("CASE FAIL")
