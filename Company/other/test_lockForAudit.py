import os
from Model.request_API import requestAPI
from Model.Logger import Logger
import platform
import pytest

class Test_lockForAudit:
    @classmethod
    def setup_class(cls):
        print("开始进入审核报告:")
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_lockForAudit(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/configure/reviewDr.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_Filename = "reviewDr.ini"
        Request = requestAPI(log, conf_Filename, section)
        result = Request.execute("config_reviewDr.xlsx", "common", "lockForAudit")


        # print(result)
        log.info("返回结果为：")
        log.info(result)
        # log.info(result["total"])
        # # print(result["users"])
        # for user in result["users"]:
        #     log.info(user)

    # role = result["data"]["role"]
    # user_id = (result["data"]["user_id"])

