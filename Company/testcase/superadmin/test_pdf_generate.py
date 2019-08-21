import os
from Model.request_API import requestAPI
from Model.Logger import Logger
from Model.config import Configure
import platform
import pytest
import time

class Test_pdf_generate:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_pdf_generate(self):
        log = Logger(os.path.basename(__file__))
        log = log.getlog()
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/configure/superAdmin.ini"
        if 'Windows' in platform.system():
            # windows os
            path = path.replace('/', '\\')
        section = "FINISH_report" #传入配置文件的section
        conf = Configure(path)
        reportIds = conf.Get_items(section)  # 取出所有setion下面的键值对,是一个元祖列表

        #获取temp.ini中的

        section1 = "login"  # 传入配置文件的section
        conf_filename = "superAdmin.ini"
        Request = requestAPI(log, conf_filename, section1)

        for reportId in reportIds:
            log.info("开始打开报告：" + str(reportId[1]) + "：")
            url = "/pdf/generate/?report_id=" + str(reportId[1])
            result = Request.execute("config_superAdmin.xlsx","pdf","pdf_generate",url)
            log.info("返回结果为：")
            # log.info(result.content)
            log.info("-------------")




