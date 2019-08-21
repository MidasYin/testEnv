import os
from Model.request_API import requestAPI
from Model.Logger import Logger
from Model.config import Configure
import platform

reportList = []

class Test_institutions:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_institutions_lanjing(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/configure/dataManager.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_filename = "dataManager.ini"
        Request = requestAPI(log, conf_filename, section)
        result = Request.execute("config_dataManager.xlsx", "common", "institutions")

        # print(result)
        log.info("返回结果为：")
        log.info(result)