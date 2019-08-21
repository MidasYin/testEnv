import os
from Model.request_API import requestAPI
from Model.Logger import Logger
from Model.config import Configure
import platform

class Test_doctorManager:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_doctorManager_All(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_filename = "superAdmin.ini"
        Request = requestAPI(log, conf_filename, section)
        result = Request.execute("config_superAdmin.xlsx", "common", "doctorManager_All")

        # print(result)
        log.info("返回结果为：")
        log.info(result)


    def test_doctorManager_EDITOR(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_filename = "superAdmin.ini"
        Request = requestAPI(log, conf_filename, section)
        result = Request.execute("config_superAdmin.xlsx", "common", "doctorManager_EDITOR")

        # print(result)
        log.info("返回结果为：")
        log.info(result)


    def test_doctorManager_AUDITOR(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_filename = "superAdmin.ini"
        Request = requestAPI(log, conf_filename, section)
        result = Request.execute("config_superAdmin.xlsx", "common", "doctorManager_AUDITOR")

        # print(result)
        log.info("返回结果为：")
        log.info(result)

    def test_doctorManager_UPLOADER(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "login"  # 传入配置文件的section
        conf_filename = "superAdmin.ini"
        Request = requestAPI(log, conf_filename, section)
        result = Request.execute("config_superAdmin.xlsx", "common", "doctorManager_UPLOADER")

        # print(result)
        log.info("返回结果为：")
        log.info(result)



