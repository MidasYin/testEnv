import os
from Model.request_API import requestAPI
from Model.Logger import Logger
import platform
import pytest

class Test_notificationsmine:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_notificationsmine(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/configure/markDr.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_Filename = "markDr.ini"
        Request = requestAPI(log, conf_Filename, section)
        result = Request.execute("config_markDr.xlsx","common","notificationsmine")


        # print(result)
        log.info("返回结果为：")
        log.info(result)



    # role = result["data"]["role"]
    # user_id = (result["data"]["user_id"])
