import os
from Model.request_API import requestAPI
from Model.Logger import Logger
import platform

reportList = []

class Test_notifications:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass


    def test_notifications(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')

        print(path)
        section = 'login'  # 传入配置文件的section
        conf_filename = "superAdmin.ini"
        Request = requestAPI(log, conf_filename,section)
        result = Request.execute("config_superAdmin.xlsx", "common", "notifications")

        # print(result)
        log.info("返回结果为：")
        print(result)
        log.info(result)